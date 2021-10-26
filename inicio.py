#Caso no seu pc não esteja automatizado,
# instale https://pyautogui.readthedocs.io/en/latest/install.html
import webbrowser
import pyautogui
import time

time.sleep(0)

# Email
webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
time.sleep(2)
# Abre linkedin
webbrowser.open("https://www.linkedin.com/in/joaovictorgb/")
time.sleep(3)
# Abre Github
webbrowser.open("https://github.com/joaovictorgb")
time.sleep(4)


# Abrir VS Code
pyautogui.hotkey("winleft")
pyautogui.write("Visual Studio")
time.sleep(2)
pyautogui.press("enter")

# Abrir Terminal
pyautogui.hotkey("winleft")
pyautogui.write("Terminal")
time.sleep(2)
pyautogui.press("enter")