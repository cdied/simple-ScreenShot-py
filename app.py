import pyautogui
import time
name = str(input("Enter you File Name >>> "))+".png"
print("ScreenShot takes in 4 sec...")
time.sleep(4)
screen = pyautogui.screenshot()
screen.save(name)
