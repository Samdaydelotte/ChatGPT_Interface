from Clear import *
from Mouse import *
from Close import *
from Highlight import *
from PhotoManagment import *
from Paste import *
from ChatLog import *
from Voice import *
import sys
import pygetwindow as gw
from PIL import ImageGrab, Image
import time
import cv2
import numpy as np
import pytesseract
from pytesseract import Output
import os
import sys

clear()


def instructions(inputImage, message, outputImage):
    # Grabs Screen, Process it to we can grab text from it. Finding TextBox
    PhotoManagment()
    # Searches image for spesifed text Highlights text
    highlight_text(inputImage, message, outputImage)
    # Gets coordinates of Text from Colored Pixels, Saves Coords For future referance, Returns tuple with x and y
    coordinatesOfItem = getCoordinates()
    return coordinatesOfItem


textBox = instructions("browser1.jpg", "message", "Highlighted.jpg")
txtFile = instructions("browser1.jpg", "notepad", "Highlighted.jpg")

# print(textBox)
# print(txtFile)

# textBox = (321, 970)
# txtFile = (1408, 145)

# Moves Mouse to textbox and Double clicks
move_mouse(textBox)
click()

# States instruction Chatgpt om how to act
#  Off for safty. Dont want to get banned
startingInstructions()

# Sleep Time For ChatGPT Response
time.sleep(10)

loop = True
while loop:
    record = input("Ready to Record. Enter 'p'")
    if record == "p":
        # Press button For microphone.
        # record speech
        # Convert speech to text
        speech = "Speech to text goes here"

        # Moves mouse to chatGPT input bar
        move_mouse(textBox)
        click()
        # Takes Speech to text and gives it to ChatGPT
        speechInstructions(speech)

        # Waits for ChatGPT's responce
        time.sleep(7)

        # Find Copy Button to Copy ChatGPT's Responce
        response = instructions("browser1.jpg", "copy", "Highlighted.jpg")
        
        # Moves mouse to Copy Coordinates, Clicks, Saves file and waits for changes to save
        move_mouse(response)
        click()

        # Moves mouse to drop point for ChatGPT's responses
        move_mouse(txtFile)
        click()
        paste()
        time.sleep(1)


        chatgptResponse = chatlogs()

        SpeakText(chatgptResponse)3
    elif record == "l":
        loop = False
    else:
        pass

# Done using Program Cleaning up Code

# Resets AIResponce.txt to default, So when I screenshot I can Latch on to the "notepad" text within
closeDownTXT()

# Removes created files
try:
    os.remove("browser1.jpg")
    # os.remove("Highlighted.jpg")
except:
    print("--- Main.py")
    print("Picture Does not Exist to Be deleted")
    sys.exit