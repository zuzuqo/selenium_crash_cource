import time

from selenium import webdriver


browser = webdriver.Chrome()

try:
    browser.get('https:duckduckgo.com')
    time.sleep(5)
    browser.get('https://google.com')

    browser.save_screenshot('screen.png')

    browser.refresh()

finally:
    browser.quit()
