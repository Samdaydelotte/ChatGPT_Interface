import cv2
import pytesseract
from pytesseract import Output
import sys

OCR_CONFIG = r'--oem 3 --psm 6'  # OCR Engine Mode (OEM) and Page Segmentation Mode (PSM)

def highlight_text(image_path, text_to_highlight, output_image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Use Tesseract to perform OCR on the image
    extracted_text = pytesseract.image_to_string(gray, config=OCR_CONFIG)


    # Check if the text to highlight is present in the extracted text
    if text_to_highlight.lower() not in extracted_text.lower():
        print(f"Text '{text_to_highlight}' not found in the image.")

        sys.exit()

    # Initialize variables
    x, y, text_width, text_height = 0, 0, 0, 0

    # Get the bounding box of the text
    try:
        h, w, _ = image.shape
        d = pytesseract.image_to_data(gray, config=OCR_CONFIG, output_type=Output.DICT)
        for i in range(len(d['text'])):
            if d['text'][i].lower() == text_to_highlight.lower():
                x, y, text_width, text_height = d['left'][i], d['top'][i], d['width'][i], d['height'][i]
                break
    except:
        print("Could not draw a box")

    # Check if the bounding box coordinates remain at their initial values
    if x == 0 and y == 0 and text_width == 0 and text_height == 0:
        print(f"Text '{text_to_highlight}' not found in the image.")
        sys.exit()

    # Draw a rectangle around the text
    cv2.rectangle(image, (x, y), (x + text_width, y + text_height), (255, 255, 0), thickness=cv2.FILLED)

    # Save the modified image
    try:
        cv2.imwrite(output_image_path, image)
        print(f"Highlighted image saved as {output_image_path}")
    except cv2.error as e:
        print(f"Error saving the highlighted image: {e}")
        sys.exit()

    return image