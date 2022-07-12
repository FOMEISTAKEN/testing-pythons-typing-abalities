import time
import keyboard
import pyperclip
import pyautogui
import keyboard

pos = 1136
pos2 = 629
def paster():
    if keyboard.read_key() == "enter":
        # time.sleep(4)
        pyautogui.moveTo(pos, pos2)
        pyautogui.doubleClick()
        pyautogui.hotkey('ctrl', 'c')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.press('backspace')
        pyautogui.press('backspace')

    elif keyboard.read_key() == "s":
        exit()
    

while True:
    paster()


#OWNER: FOME DO NOY STEAL





