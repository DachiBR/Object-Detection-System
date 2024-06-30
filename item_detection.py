import cv2
import numpy as np

def detect_items(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and improve contour detection
    blurred = cv2.GaussianBlur(gray, (11, 11), 0)

    # Apply adaptive thresholding
    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)

    # Perform morphological operations to remove noise
    kernel = np.ones((5, 5), np.uint8)
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    morph = cv2.erode(morph, kernel, iterations=1)
    morph = cv2.dilate(morph, kernel, iterations=1)

    # Apply edge detection (Canny)
    edged = cv2.Canny(morph, 50, 150)

    # Dilate the edges to ensure proper contour detection
    dilated = cv2.dilate(edged, kernel, iterations=2)

    # Find contours
    contours, _ = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Filter contours by area and aspect ratio
    min_area = 100  # Minimum area of a contour to be considered an item
    max_area = 10000  # Maximum area of a contour to be considered an item
    filtered_contours = []
    for cnt in contours:
        area = cv2.contourArea(cnt)
        x, y, w, h = cv2.boundingRect(cnt)
        aspect_ratio = float(w) / h
        if min_area < area < max_area and 0.2 < aspect_ratio < 5.0:  # Adjust aspect ratio range as needed
            filtered_contours.append(cnt)

    return len(filtered_contours), filtered_contours
