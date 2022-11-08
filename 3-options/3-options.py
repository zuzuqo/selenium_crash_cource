import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('useAutomationExtension', False)
options.headless = True
browser = webdriver.Chrome(options=options)

try:
#    browser.get('https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html')
    while True:
        browser.get('https://mynickname.com/ru/generate')
        browser.find_element(By.XPATH, '//*[@id="generate"]').click()
        nick = browser.find_element(By.XPATH, '//*[@id="register"]').get_attribute('href').split('nick=')[-1]
        print(nick)
        time.sleep(1)

finally:
    browser.quit()
