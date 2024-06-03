import pyautogui as pg
import time
import random as r
from datetime import datetime

 
time.sleep(2)
i=1

while 1 :
    x,y=r.randint(1074,1151),r.randint(354,433)
   
    print("No. of times- ", i)

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    pg.moveTo(x,y,2)
    pg.leftClick()
    time.sleep(5)
    i += 1
