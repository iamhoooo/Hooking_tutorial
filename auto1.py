import pyautogui
import time

pyautogui.press('win')
pyautogui.typewrite('note')

pyautogui.press('enter')
time.sleep(1)

pyautogui.typewrite('hello')
time.sleep(1)

pyautogui.hotkey('alt','f4')
time.sleep(1)

pyautogui.press('n')