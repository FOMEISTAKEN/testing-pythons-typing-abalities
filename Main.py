import random
import time
import pyautogui
import keyboard
import pygetwindow as gw



slowmode = input("does da server have slowmode?: ")
number = int(input("what's the current number? : "))
num = number + 1
delay = random.uniform(1.6, 2.9)

#NOTE the enter the chill zone thing comes at 1042:680 when discord is at the lower right corner of da screen
pos1 = 1042
pos2 = 680

interval = random.uniform(0.03, 0.07)

howtocount = int(input("do u want to add or to go to specific number? (1=add, 2=specific number): "))

if howtocount == 1:
    add = int(input("how much u wanna add?: "))

elif howtocount ==2:
    number_difference = int(input("Till how much u wanna count? : "))

else:
    print("error")




time.sleep(4)
gap = random.uniform(0.25, 0.91)
typergap = random.uniform(4, 4
)
time.sleep(5)

if howtocount == 1:
    if slowmode == "yes" or slowmode == "y":
        while num < num+add+1:
            pyautogui.typewrite(str(num),interval=0.05)
            time.sleep(typergap)
            pyautogui.press( 'enter' )
            num += 1
            # countingWindow = gw.getWindowsWithTitle('💯count-to-600000💯 - Opera' )[0]
            # countingWindow.activate()

    elif slowmode == "no" or slowmode == "n":
            while num < num+add+1:
                time.sleep(delay) #TODO comment out this line to turn on burst fire mode (WARNING MAY CAUSE PC TO CRASH)
                pyautogui.typewrite(str(num),interval=interval)
                pyautogui.press( 'enter' )
                num += 1
                # countingWindow = gw.getWindowsWithTitle('💯count-to-600000💯 - Opera' )[0]
                # countingWindow.activate()
                # pyautogui.moveTo(pos1, pos2)
                
                # pyautogui.click()

                
    else:
        print("error")

elif howtocount == 2:
    if slowmode == "yes" or slowmode == "y":
        while num < number_difference+1:
            pyautogui.typewrite(str(num),interval=0.05)
            time.sleep(typergap)
            pyautogui.press( 'enter' )
            num += 1
            # countingWindow = gw.getWindowsWithTitle('💯count-to-600000💯 - Opera' )[0]
            # countingWindow.activate()

    elif slowmode == "no" or slowmode == "n":
            while num < number_difference+1:
                time.sleep(delay)
                pyautogui.typewrite(str(num),interval=interval)
                pyautogui.press( 'enter' )
                num += 1
                # countingWindow = gw.getWindowsWithTitle('💯count-to-600000💯 - Opera' )[0]
                # countingWindow.activate()

    elif keyboard.read_key() == "s":
        exit()
    else:
        print("error")



else:

    print("error")


# def activator():
# #     countingWindow = gw.getWindowsWithTitle('💯count-to-600000💯 - Opera' )[0]
# #     countingWindow.activate()


# # while True:
# #     activator()

  ##
  ##
  ##
  ##
  ##
  ##
  ##

