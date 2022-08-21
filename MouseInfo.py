import pyautogui
import time
import keyboard

while True:
    x, y = pyautogui.position()
    print("X: ",x,", Y: ",y)
    print(pyautogui.pixel(x,y))
    time.sleep(1)

