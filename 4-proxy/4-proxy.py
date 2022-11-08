import time
from selenium import webdriver


# https://www.youtube.com/watch?v=tx5vvJwX-f0&list=PL6plRXMq5RABXsb0-B0CrWniWBoFZOL20&index=5
option = webdriver.ChromeOptions()
option.add_argument('--proxy-server=IP_ADDRESS:PORT')
browser = webdriver.Chrome(options=option)
browser.get('https://icanhazip.com')
browser.quit()
