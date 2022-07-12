import random
import time
import pyautogui
number = int(input("what's the current number? : "))
num = number + 1
number_difference = int(input("Till how much u wanna count? : "))
time.sleep(4)
gap = random.uniform(1, 2.424)



while num < number_difference+1:
    time.sleep(gap)
    pyautogui.typewrite(str(num))
    time.sleep(0.2)
    pyautogui.press( 'enter' )
    num += 1

  ##
  ##
  ##
  ##
  ##
  ##
  ##
