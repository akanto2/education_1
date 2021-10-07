import time

from selenium import webdriver

browser = webdriver.Chrome('./chromedriver.exe')

browser.get('http://www.naver.com')

time.sleep(5)

browser.close()
