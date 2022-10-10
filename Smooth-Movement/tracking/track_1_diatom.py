from pathlib import Path
import json
import numpy as np
import cv2  # type: ignore
import plotly.express as px  # type: ignore
import pandas as pd  # type: ignore
from typing import Dict, Any


VIDEO_DIR_PATH = Path("Smooth-Movement/data/40x_100fps_b5/")
VIDEO_NAME = "40x_100fps_b5_trimmed_1"
VIDEO_PATH = VIDEO_DIR_PATH / (VIDEO_NAME + ".avi")
TRACKING_VID_PATH = VIDEO_DIR_PATH / (VIDEO_NAME + "_track" + ".avi")
TRACKING_IMG_PATH = VIDEO_DIR_PATH / (VIDEO_NAME + "_track" + ".png")
TRACKING_POINT_PATH = VIDEO_DIR_PATH / (VIDEO_NAME + "_track" + ".json")
SCALE_UNIT_PATH = Path(
    "Smooth-Movement/data/40x_100fps_b5/40x_100fps_b5_scale_unit.json"
)
GET_ANGLE_STATS = False

# Parameters for lucas kanade optical flow
LK_PARAMS = dict(
    winSize=(15, 15),
    maxLevel=2,
    criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03),
)


def mouse_callback(event, x, y, flags, params):
    if event == 1:  # Left click
        params.append([x, y])


def get_starting_point(
    first_frame,
):
    instructions = "Mouse left click to choose starting point, then press q."
    cv2.namedWindow(instructions)
    left_click = list()
    cv2.setMouseCallback(instructions, mouse_callback, left_click)
    print(instructions)
    cv2.imshow(instructions, first_frame)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    if len(left_click) == 0:
        raise ValueError("Not detected left click and starting point.")
    return left_click


def tracking_candidates(
    img,
):
    feature_params = dict(maxCorners=10, qualityLevel=0.3, minDistance=7, blockSize=7)
    p0 = cv2.goodFeaturesToTrack(img, mask=None, **feature_params)
    return p0


def track_1_diatom(
    vid_path,
    output_track_video_path: Path,
    lk_params: Dict[str, Any],
    output_track_img_path: Path,
    output_track_points_path: Path,
    scale_unit_path: Path,
    get_angle_stats: bool,
):
    color = np.random.randint(0, 255, (100, 3))
    cap = cv2.VideoCapture(vid_path.as_posix())
    video_frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    writerInit = False
    # Take first frame to find starting point
    ret, old_frame = cap.read()
    old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
    mask = np.zeros_like(old_frame)
    # Get tracking point
    # tracking_point = get_starting_point(old_frame)
    tracking_point_pix = [[661, 22]]
    cur_track_point = np.array(tracking_point_pix, dtype=np.float32)
    cur_track_point = np.reshape(cur_track_point, newshape=(-1, 1, 2))
    tracking_points = cur_track_point.copy()
    while 1:
        ret, frame = cap.read()
        if not ret:
            break
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # calculate optical flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(
            old_gray, frame_gray, cur_track_point, None, **lk_params
        )
        if p1 is not None:
            good_new = p1[st == 1]
            good_old = cur_track_point[st == 1]
        for i, (new, old) in enumerate(zip(good_new, good_old)):
            a, b = new.ravel()
            c, d = old.ravel()
            mask = cv2.line(
                mask, (int(a), int(b)), (int(c), int(d)), color[i].tolist(), 2
            )
            frame = cv2.circle(frame, (int(a), int(b)), 5, color[i].tolist(), -1)
        img = cv2.add(frame, mask)
        if not writerInit:
            h, w, _ = img.shape
            out_vid = cv2.VideoWriter(
                output_track_video_path.as_posix(),
                fourcc,
                video_frame_rate,
                (1280, 720),
            )
            writerInit = True
        out_vid.write(img)
        cv2.imshow("frame", img)
        k = cv2.waitKey(int(1000 / video_frame_rate)) & 0xFE
        if k == 26:
            break
        old_gray = frame_gray.copy()
        cur_track_point = good_new.reshape(-1, 1, 2)
        tracking_points = np.append(tracking_points, cur_track_point, axis=0)
    cv2.imwrite(output_track_img_path.as_posix(), img)
    cv2.destroyAllWindows()
    track_scaled = scale_tracking_points(tracking_points, scale_unit_path)
    # Rotate to 1 dim:
    # To be checked with 2 tracking points
    init_points = track_scaled[0]
    track_sub = np.subtract(track_scaled, init_points)
    track_sub_y = track_sub[:, :, 1]
    track_sub_x = track_sub[:, :, 0]
    track_1_axis, phi = cart2pol(track_sub_x, track_sub_y)
    if get_angle_stats:
        check_phi_histogram_per_line(phi)
    with open(output_track_points_path, "w") as f:
        json.dump(track_1_axis.tolist(), f, indent=4)
    pass


def check_phi_histogram_per_line(
    phi: np.ndarray,
) -> None:
    phi_deg = phi[1:] / np.pi * 180
    col_name = "Angle (degrees)"
    phi_df = pd.DataFrame(phi_deg, columns=[col_name])
    fig = px.histogram(phi_df, title="Line angle distribution", x=col_name)
    fig.show()
    print(f"STD - {np.std(phi_deg)}")
    print(f"Mean angle (degrees)- {np.mean(phi_deg)}")


def cart2pol(x, y):
    rho = np.sqrt(x**2 + y**2)
    phi = np.arctan2(y, x)
    return (rho, phi)


def pol2cart(rho, phi):
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return (x, y)


def scale_tracking_points(
    tracking_points: np.ndarray,
    scale_unit_path: Path,
):
    with open(scale_unit_path, "r") as f:
        scale_unit = json.load(f)
    return np.multiply(tracking_points, scale_unit["scale"])


if __name__ == "__main__":
    track_1_diatom(
        VIDEO_PATH,
        TRACKING_VID_PATH,
        LK_PARAMS,
        TRACKING_IMG_PATH,
        TRACKING_POINT_PATH,
        SCALE_UNIT_PATH,
        GET_ANGLE_STATS,
    )
