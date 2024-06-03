import pyautogui
import random
import time

pyautogui.FAILSAFE = False

def move_mouse():
    while True:
        x = random.randint(0, 1920)  
        y = random.randint(0, 1080)
        pyautogui.moveTo(x, y, duration=0.25)
        time.sleep(5)

move_mouse()
