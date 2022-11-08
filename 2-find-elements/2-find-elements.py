import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.get('https:youtube.com')

    html = browser.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.DOWN)
    html.send_keys(Keys.DOWN)
    html.send_keys(Keys.DOWN)
    html.send_keys(Keys.DOWN)
    html.send_keys(Keys.DOWN)

    titles = browser.find_elements(By.XPATH, '//*[@id="video-title-link"]')
    for title in titles:
        video_title = title.get_attribute('title')
        print(video_title)
        
    login = browser.find_element(By.XPATH, '//*[@id="buttons"]/ytd-button-renderer')
    login.click()
    browser.find_element(By.XPATH, '//*[@id="identifierId"]').send_keys('example@gmail.com')
    browser.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()

    time.sleep(5)

finally:
    browser.quit()




