import pyautogui
import time
import pyperclip

# print(pyautogui.position())
# time.sleep(3)
# pyautogui.moveTo(500, 500, 2) #x500 y500 위치로 2초동안 이동

# 브라우저 열기
pyautogui.hotkey("winleft", "r")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)


# 네이버 로그인 페이지로 이동
naver_url = "https://nid.naver.com/nidlogin.login"
pyautogui.write(naver_url)
pyautogui.press("enter")
time.sleep(2)

# 아이디와 비밀번호 입력
pyautogui.write("abc")
pyautogui.press("tab")
pyautogui.write("def")
pyautogui.press("enter")

# id_x, id_y = pyautogui.locateCenterOnScreen("naver_id.png", confidence=0.8)
# password_x, password_y = pyautogui.locateCenterOnScreen("naver_password.png", confidence=0.8)

# 로그인 버튼 클릭
# login_x, login_y = pyautogui.locateCenterOnScreen("naver_login.png", confidence=0.8)
# pyautogui.click(1895,1026)