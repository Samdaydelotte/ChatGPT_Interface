from Clear import *
import cv2
import numpy as np
import pyautogui
import random
import sys

# clear()


def load_image(file_path):
    try:
        img = cv2.imread(file_path)
        if img is None:
            print(f"\n--- Mouse.py\n--- Failed to load '{file_path}'. Check file path and integrity.")
            sys.exit()
        return img
    except Exception as e:
        print(f"--- Mouse.py\n--- An error occurred while loading the image: {e}")
        sys.exit()

def find_yellow_pixels(image):
    yellow = [255, 255, 0]
    try:
        Y, X = np.where(np.all(image == yellow, axis=-1))
        return list(zip(X, Y))
    except Exception as e:
        print(f"--- Mouse.py\n--- An error occurred while finding yellow pixels: {e}")
        sys.exit()


def calculate_middle(coordinates):
    if not coordinates:
        print("No coordinates provided.")
        return None

    total_x = 0
    total_y = 0

    for coordinate in coordinates:
        total_x += coordinate[0]
        total_y += coordinate[1]

    average_x = total_x / len(coordinates)
    average_y = total_y / len(coordinates)

    return int(average_x), int(average_y)


def getCoordinates():
    file_path = 'Highlighted.jpg'

    # Load image
    img = load_image(file_path)

    # Find yellow pixels
    coordinates = find_yellow_pixels(img)
    # print(coordinates)

    calculate_middle(coordinates)

    # Move mouse to a random yellow pixel
    middle_value = calculate_middle(coordinates)

    x = middle_value[0]
    y = middle_value[1]
    return middle_value


def move_mouse(middle_value):
    if not middle_value:
        print("--- Mouse.py\n--- No Yellow pixels Found\nOr No Cordsinates Found")
        sys.exit()

    x = middle_value[0]
    y = middle_value[1]

    pyautogui.moveTo(x, y, duration=1)

    return middle_value


def click():
    pyautogui.doubleClick()

def save():
    pyautogui.hotkey('ctrl', 's')

if __name__ == "__main__":
    getCoordinates()

# Test