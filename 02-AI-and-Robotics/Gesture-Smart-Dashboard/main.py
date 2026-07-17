"""
Gesture-Controlled Smart Dashboard

Main application:
- Tracks a colored object using computer vision.
- Uses the tracked object as a virtual pen.
- Displays the drawing in real time.

Keyboard Controls:
    C : Clear the drawing canvas
    Q : Quit the application
"""

import sys
import cv2

from modules.camera_utils import open_laptop_camera
from modules import color_tracker
from modules.virtual_paint import VirtualCanvas


# Current operating mode
MODE_PAINT = "paint"


def draw_hud(frame, mode):
    """
    Draw the Heads-Up Display (HUD).

    Displays:
    - Current application mode.
    - Available keyboard shortcuts.
    """

    # Display current mode
    cv2.putText(
        frame,
        f"Mode: {mode}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2,
    )

    # Display keyboard commands
    cv2.putText(
        frame,
        "C: Clear | Q: Quit",
        (10, frame.shape[0] - 15),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        (200, 200, 200),
        1,
    )

    return frame


def main():
    """
    Main application loop.

    Workflow:
    1. Open the camera.
    2. Capture video frames.
    3. Detect the colored object.
    4. Draw its movement on the virtual canvas.
    5. Merge the canvas with the live frame.
    6. Display the final result.
    """

    print("Starting camera... Press Q to quit.")

    # Open the laptop camera
    cap = open_laptop_camera()

    # Exit if the camera cannot be opened
    if cap is None or not cap.isOpened():
        print("Error: Unable to open the camera.")
        sys.exit()

    # Capture the first frame to determine frame size
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to capture the first frame.")
        sys.exit()

    # Get frame dimensions
    height, width = frame.shape[:2]

    # Create the virtual drawing canvas
    canvas = VirtualCanvas(width, height)

    # Set the current operating mode
    mode = MODE_PAINT

    # Main processing loop
    while True:

        # Read a new frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Flip the frame horizontally for a mirror effect
        frame = cv2.flip(frame, 1)

        # Create a copy of the current frame for display
        display_frame = frame.copy()

        if mode == MODE_PAINT:

            # Generate a binary mask for the selected color
            mask = color_tracker.create_mask(frame)

            # Detect the center of the tracked object
            result = color_tracker.find_object_center(mask)

            if result:

                # Extract object center and radius
                cx, cy, radius = result

                # Draw a circle around the detected object
                cv2.circle(
                    frame,
                    (cx, cy),
                    max(radius, 5),
                    (0, 255, 0),
                    2,
                )

                # Store the detected point
                canvas.add_point((cx, cy))

            else:
                # Break the drawing stroke if no object is detected
                canvas.add_point(None)

            # Draw all stored points
            canvas.draw()

            # Merge the drawing with the live camera frame
            display_frame = canvas.merge_with_frame(frame)

        # Draw the application HUD
        display_frame = draw_hud(display_frame, mode)

        # Display the final output
        cv2.imshow("Smart Dashboard", display_frame)

        # Read keyboard input
        key = cv2.waitKey(1) & 0xFF

        # Quit application
        if key == ord("q"):
            break

        # Clear the drawing canvas
        elif key == ord("c"):
            canvas.clear()

    # Release camera resources
    cap.release()

    # Close all OpenCV windows
    cv2.destroyAllWindows()

    print("Camera closed successfully.")


if __name__ == "__main__":
    main()