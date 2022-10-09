import numpy as np
import cv2
from pathlib import Path


VIDEO_PATH = Path("Smooth-Movement/data/40x_100fps_b5_trimmed_1.avi")
TRACKING_VID_PATH = Path("Smooth-Movement/data/40x_100fps_b5_trimmed_1_track.avi")
TRACKING_IMG_PATH = Path("Smooth-Movement/data/40x_100fps_b5_trimmed_1_track.png")

# Parameters for lucas kanade optical flow
lk_params = dict(
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
    output_track_img_path: Path,
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
    tracking_point = np.array(tracking_point_pix, dtype=np.float32)
    tracking_point = np.reshape(tracking_point, newshape=(-1, 1, 2))
    while 1:
        ret, frame = cap.read()
        if not ret:
            print("No frames grabbed!")
            break
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # calculate optical flow
        p1, st, err = cv2.calcOpticalFlowPyrLK(
            old_gray, frame_gray, tracking_point, None, **lk_params
        )
        if p1 is not None:
            good_new = p1[st == 1]
            good_old = tracking_point[st == 1]
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
        tracking_point = good_new.reshape(-1, 1, 2)
    img
    cv2.destroyAllWindows()
    pass


if __name__ == "__main__":
    track_1_diatom(VIDEO_PATH, TRACKING_VID_PATH, TRACKING_IMG_PATH)
