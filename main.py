from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()

driver.get('https://coinmarketcap.com/currencies/ethereum/')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

while True:
    driver.refresh()

    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    price = soup.find('div', {'class': 'priceValue'}).text
    print(price)
driver.quit()

