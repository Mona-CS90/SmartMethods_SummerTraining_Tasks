"""
Color Calibration Tool
Run this script to determine the optimal HSV range
for the object you want to track.
"""

import cv2
import numpy as np
from modules.camera_utils import open_laptop_camera


# Empty callback function required by OpenCV trackbars
def nothing(x):
    pass


def main():

    # Open the laptop camera
    cap = open_laptop_camera()

    # Exit if the camera cannot be opened
    if cap is None or not cap.isOpened():
        print("Error: Unable to open the camera.")
        return

    # Create a window to hold HSV trackbars
    cv2.namedWindow("Trackbars")

    # Create HSV sliders for minimum and maximum values
    cv2.createTrackbar("H Min", "Trackbars", 94, 179, nothing)
    cv2.createTrackbar("H Max", "Trackbars", 126, 179, nothing)

    cv2.createTrackbar("S Min", "Trackbars", 80, 255, nothing)
    cv2.createTrackbar("S Max", "Trackbars", 255, 255, nothing)

    cv2.createTrackbar("V Min", "Trackbars", 2, 255, nothing)
    cv2.createTrackbar("V Max", "Trackbars", 255, 255, nothing)

    print("Adjust the sliders until only the target object appears in the mask.")
    print("Press 's' to save the values or 'q' to quit.")

    while True:

        # Capture a frame from the camera
        ret, frame = cap.read()

        if not ret:
            break

        # Convert the frame from BGR to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Read current HSV values from the sliders
        h_min = cv2.getTrackbarPos("H Min", "Trackbars")
        h_max = cv2.getTrackbarPos("H Max", "Trackbars")

        s_min = cv2.getTrackbarPos("S Min", "Trackbars")
        s_max = cv2.getTrackbarPos("S Max", "Trackbars")

        v_min = cv2.getTrackbarPos("V Min", "Trackbars")
        v_max = cv2.getTrackbarPos("V Max", "Trackbars")

        # Create lower and upper HSV boundaries
        lower = np.array([h_min, s_min, v_min])
        upper = np.array([h_max, s_max, v_max])

        # Generate the binary mask
        mask = cv2.inRange(hsv, lower, upper)

        # Apply the mask to visualize the detected object
        result = cv2.bitwise_and(frame, frame, mask=mask)

        # Display original frame, mask, and filtered result
        cv2.imshow("Camera", frame)
        cv2.imshow("Mask", mask)
        cv2.imshow("Result", result)

        key = cv2.waitKey(1) & 0xFF

        # Print HSV values when 's' is pressed
        if key == ord("s"):

            print(f"\nDEFAULT_LOWER = np.array([{h_min}, {s_min}, {v_min}])")
            print(f"DEFAULT_UPPER = np.array([{h_max}, {s_max}, {v_max}])")

            print("Copy these values into color_tracker.py")

        # Exit when 'q' is pressed
        elif key == ord("q"):
            break

    # Release camera resources
    cap.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()