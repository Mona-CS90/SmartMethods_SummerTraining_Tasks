
import cv2
import numpy as np

DEFAULT_LOWER = np.array([94, 80, 2])
DEFAULT_UPPER = np.array([126, 255, 255])

MIN_CONTOUR_AREA = 400

#Used HSV more stable and easy to isolate coulrs .
def create_mask(frame, lower=DEFAULT_LOWER, upper=DEFAULT_UPPER):
    """يحول الإطار إلى HSV وينشئ قناع (mask) للون المطلوب"""
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #Produce photo with White and Black 
    mask = cv2.inRange(hsv, lower, upper)
#Remove noise like white dots , erode to delete noise ,and dilate resize the body to the real size
    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.erode(mask, kernel, iterations=1)
    mask = cv2.dilate(mask, kernel, iterations=2)
    return mask


def find_object_center(mask):
    """
    Find the largest detected object in the binary mask.

    Returns:
        (center_x, center_y, radius): Coordinates and radius of the detected object.
        None: If no valid object is found.
    """

    # Detect all external contours (connected white regions) in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Return None if no contours are detected
    if not contours:
        return None

    # Select the contour with the largest area
    largest = max(contours, key=cv2.contourArea)

    # Ignore small contours to reduce noise
    if cv2.contourArea(largest) < MIN_CONTOUR_AREA:
        return None

    # Compute the minimum enclosing circle around the detected object
    (x, y), radius = cv2.minEnclosingCircle(largest)

    # Return the center coordinates and radius as integers
    return int(x), int(y), int(radius)