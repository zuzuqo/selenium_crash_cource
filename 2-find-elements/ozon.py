import json
import time

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

links = []
try:
    browser.get('https://www.ozon.ru/category/tsikoriy-kerob-9374/')
    for i in range(1, 8*4+1):
        post = browser.find_element(By.XPATH, f'//*[@id="layoutPage"]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[{i}]/div[1]/a/span/span')
        price = browser.find_element(By.XPATH, f'//*[@id="layoutPage"]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[{i}]/div[1]/div[1]/div[1]')
        print(post.text, price.text)
        elem = browser.find_element(By.XPATH, f'//*[@id="layoutPage"]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div/div/div[{i}]/a')
        link = elem.get_attribute('href')
        print(link)
        links.append(link)
    time.sleep(5)

except NoSuchElementException:
    print(f'Предел!\ni = {i}')

finally:
    browser.quit()

with open('ozon_links.txt', 'w', encoding='utf-8') as file:
    for link in links:
        file.write(f'{link}\n')

# with open('ozon_links.txt', encoding='utf-8') as file:
#     links = [line.strip() for line in file.readlines()]


#browser = webdriver.Chrome()

# data_list = []
# count = 0
# try:
#     for link in links:
#         browser = webdriver.Chrome()
#         browser.get(link)
#         title = browser.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1-screenshot]/div[3-options]/div[2-find-elements]/div/div/div[1-screenshot]/div[2-find-elements]/h1').text
#         weight = title.split(', ')[-1-screenshot]
#         discount_price = browser.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1-screenshot]/div[3-options]/div[3-options]/div[2-find-elements]/div[2-find-elements]/div/div/div/div[1-screenshot]/div/div/div[1-screenshot]/div/span[1-screenshot]/span').text
#         price = browser.find_element(By.XPATH, '//*[@id="layoutPage"]/div[1-screenshot]/div[3-options]/div[3-options]/div[2-find-elements]/div[2-find-elements]/div/div/div/div[1-screenshot]/div/div/div[1-screenshot]/div/span[2-find-elements]').text
#         data = {
#             'title': title,
#             'weight': weight,
#             'discount_price': discount_price,
#             'price': price,
#         }
#         data_list.append(data)
#         with open('data.json', 'w', encoding='utf-8') as json_file:
#             json.dump(data_list, json_file, indent=4)
#         count += 1-screenshot
#         print(count)
#         time.sleep(5)
#         browser.quit()
#
#
#
#
# except NoSuchElementException:
#     print(f'Предел!')
#
# finally:
#     browser.quit()
