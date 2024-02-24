import cv2
from PIL import ImageGrab
import numpy as np


# Functions
def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def PhotoManagment():
    # Gets Screen grab
    img = ImageGrab.grab()

    # Converts image from PIL to numpy
    img_array = np.array(img)

    inverted_image = cv2.bitwise_not(img_array)

    grey_image = convert_to_grayscale(inverted_image)

    thresh, img_bw = cv2.threshold(grey_image, 180, 200, cv2.THRESH_BINARY)

    cv2.imwrite("browser1.jpg", img_bw)
    # Test