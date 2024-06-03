def move_mouse():
    import pyautogui
    import random
    import time
    while True:
        x = random.randint(0,1920)
        y = random.randint(0,1080)
        pyautogui.moveTo(x, y, duration=0.25)
        time.sleep(5)

move_mouse()