from time import sleep
import pyautogui as spam

limite_msg = int(input("Enter message number: "))
msg = input("Type your message: ")
i = 0
sleep(2)

while (i < limite_msg):
    spam.typewrite(msg)
    spam.press("enter")
    sleep(1)
    i += 1