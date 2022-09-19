from operator import length_hint
import numpy as np
import cv2 
import json

IMG_TO_CALIBRATE = "Smooth-Movement/data/40x_100fps_b5_scale_bar.jpg"
LENGTH_IN_U_METERS = 50.0
SCALE_SAVE_PATH = "Smooth-Movement/data/40x_100fps_b5_scale_unit.json"
# Scale will fulfill the equation:
# Length in u meters = scale * amount of pixels


def mouse_callback(event, x, y, flags, params):
    if event == 1: # Left click
        params.append([x, y])
        print(params)


def calibrate_image(
    img_to_calibrate: str,
    length_in_u_meters: float,
    scale_save_path: str,
) -> None:
    left_click = list()
    img = cv2.imread(img_to_calibrate)
    scale=1.5
    window_width = int(img.shape[1] * scale)
    window_height = int(img.shape[0] * scale)
    cv2.namedWindow('image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('image', window_width, window_height)
    #set mouse callback function for window
    cv2.setMouseCallback('image', mouse_callback, left_click)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    amount_pixels = left_click[1][0] - left_click[0][0]
    picture_scale = length_in_u_meters / amount_pixels
    picture_scale_round = {
        'scale': round(picture_scale, 5)
    }
    print(picture_scale_round)
    with open(scale_save_path, "w") as f:
        json.dump(picture_scale_round, f)


if __name__ == '__main__':
    calibrate_image(
        IMG_TO_CALIBRATE, 
        LENGTH_IN_U_METERS,
        SCALE_SAVE_PATH,
    )