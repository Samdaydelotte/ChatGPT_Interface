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




def instructions(inputImage, message, outputImage):
    # Grabs Screen, Process it to we can grab text from it. Finding TextBox
    PhotoManagment()
    # Searches image for spesifed text Highlights text
    highlight_text(inputImage, message, outputImage)
    # Gets coordinates of Text from Colored Pixels, Saves Coords For future referance, Returns tuple with x and y
    coordinatesOfItem = getCoordinates()
    return coordinatesOfItem


def mainLoop():
    clear()

    textBox = instructions("browser1.jpg", "message", "Highlighted.jpg")
    txtFile = instructions("browser1.jpg", "notepad", "Highlighted.jpg")

    # Moves Mouse to textbox and Double clicks
    move_mouse(textBox)
    click()
    # States instruction Chatgpt om how to act
    startingInstructions()

    # Sleep Time For ChatGPT Response
    # time.sleep(1)

    loop = True
    while loop:
        record = input("Ready to Record. Enter 'p'")
        if record == "p":
            # Records speech Convert speech to text
            speech = SpeakNow()

            # Moves mouse to chatGPT input bar
            move_mouse(textBox)
            click()
            # Takes Speech to text and gives it to ChatGPT
            speechInstructions(speech)

            # Waits for ChatGPT's responce
            time.sleep(3)
            pyautogui.hotkey("ctrl", "shift", "c")

            # Moves mouse to drop point for ChatGPT's responses
            move_mouse(txtFile)
            click()
            paste()
            time.sleep(2)
            save()


            chatgptResponse = chatlogs()

            SpeakText(chatgptResponse)
            closeDownTXT()
        elif record == "l":
            loop = False
        else:
            pass

    # Done using Program Cleaning up Code
    # Resets AIResponce.txt to default, So when I screenshot I can Latch on to the "notepad" text within
    # closeDownTXT()

    # Removes created files
    try:
        os.remove("browser1.jpg")
        os.remove("Highlighted.jpg")
    except:
        print("--- Main.py")
        print("Picture Does not Exist to Be deleted")
        sys.exit

mainLoop()