import pyautogui
import time

# stop mouse if is moving
pyautogui.FAILSAFE = True

# open browser
pyautogui.hotkey("win")
pyautogui.write("Chrome", interval=0.1)
pyautogui.press("enter")

# search web
pyautogui.moveTo(800,600, duration=1)
pyautogui.click()
pyautogui.write("wikipedia.org", interval=0.1)
pyautogui.press("enter")

# search on site
time.sleep(2)
pyautogui.write("Linus Torvald", interval=0.1)
pyautogui.press("enter")
time.sleep(2)
pyautogui.moveTo(300,600, duration=1)
pyautogui.click()
time.sleep(2)

# screenshot on page
img = pyautogui.screenshot()
img.save("picture.png")