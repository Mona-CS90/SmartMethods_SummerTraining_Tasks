"""
Virtual Paint Module
Stores the tracked object path and draws it on a separate canvas.
"""

import cv2
import numpy as np


class VirtualCanvas:
    """
    A class responsible for managing the virtual drawing canvas.
    It stores tracked points and renders them as continuous lines.
    """

    def __init__(self, width, height, color=(255, 0, 255), thickness=6):
        # Create an empty black canvas with the same size as the camera frame
        self.canvas = np.zeros((height, width, 3), dtype=np.uint8)

        # Store all tracked points
        self.points = []

        # Drawing color (default: purple)
        self.color = color

        # Brush thickness
        self.thickness = thickness

    def add_point(self, point):
        """
        Add a new tracking point.

        Args:
            point: (x, y) coordinates or None to indicate a break in drawing.
        """
        self.points.append(point)

    def draw(self):
        """
        Draw lines between consecutive points.

        If either point is None, drawing is skipped to avoid
        connecting separate strokes.
        """
        for i in range(1, len(self.points)):

            # Skip drawing when the pen is lifted
            if self.points[i - 1] is None or self.points[i] is None:
                continue

            # Draw a line between two consecutive points
            cv2.line(
                self.canvas,
                self.points[i - 1],
                self.points[i],
                self.color,
                self.thickness,
            )

        return self.canvas

    def clear(self):
        """
        Clear the entire canvas and remove all stored points.
        """
        self.canvas[:] = 0
        self.points = []

    def merge_with_frame(self, frame):
        """
        Merge the drawing canvas with the live camera frame.

        Steps:
        1. Convert the canvas to grayscale.
        2. Create an inverse binary mask.
        3. Remove drawing pixels from the original frame.
        4. Overlay the drawing onto the frame.
        5. Return the final merged image.
        """

        # Convert canvas to grayscale
        gray = cv2.cvtColor(self.canvas, cv2.COLOR_BGR2GRAY)

        # Create an inverse binary mask
        _, mask_inv = cv2.threshold(gray, 20, 255, cv2.THRESH_BINARY_INV)

        # Convert mask back to BGR for bitwise operations
        mask_inv = cv2.cvtColor(mask_inv, cv2.COLOR_GRAY2BGR)

        # Remove drawing area from the original frame
        frame_bg = cv2.bitwise_and(frame, mask_inv)

        # Overlay the virtual drawing onto the frame
        result = cv2.bitwise_or(frame_bg, self.canvas)

        return result