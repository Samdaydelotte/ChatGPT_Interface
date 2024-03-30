import pygetwindow as gw
import time
import sys
import pyautogui

def closeApps():
    try:
        BROWSER = gw.getWindowsWithTitle("ChatGPT - Personal")[0]
        CODETWO = gw.getWindowsWithTitle("mains")[0]
    except:
        print("---Close.py\n---Open Edge")
        sys.exit()
    # Closes all open apps
    ActiveApplications = gw.getAllTitles()
    for app_title in ActiveApplications:
        application = gw.getWindowsWithTitle(app_title)[0]
        application.minimize()

    BROWSER.maximize()
    pyautogui.hotkey("win", "left")
    CODETWO.maximize()
    time.sleep(1)
    pyautogui.hotkey("win", "right")
    try:
        customTab = gw.getWindowsWithTitle("You Idiot")[0]
    except:
        print("Fail")
    customTab.maximize()