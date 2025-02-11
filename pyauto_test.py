import pyautogui
import keyboard
import random
import time

res = pyautogui.position()

while keyboard.is_pressed('r') == False:
    while keyboard.is_pressed('f') == True:
        mousePos = pyautogui.position()
        pyautogui.click(mousePos.x, mousePos.y, 10, .001, 'left')
print(res)