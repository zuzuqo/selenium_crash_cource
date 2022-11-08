import time
import pickle
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://coinmarketcup.com')
time.sleep(10)
pickle.dump(browser.get_cookies(), open('session', 'wb'))
print('cookies saved')

for cookie in pickle.load(open('session', 'rb')):
    browser.add_cookie(cookie)

print('cookies loaded')
browser.get('https://coinmarketcup.com')

browser.quit()
