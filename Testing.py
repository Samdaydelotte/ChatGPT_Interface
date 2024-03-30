import pygetwindow as gw
import time
import sys
import pyautogui

ActiveApplications = gw.getAllTitles()

print(ActiveApplications)


try:
    BROWSER = gw.getWindowsWithTitle("Chat")[0]
    CODE = gw.getWindowsWithTitle("mains")[0]
    CODETWO = gw.getWindowsWithTitle("mainy")[0]
except:
    print("---Close.py\n---Open Edge")
    sys.exit()