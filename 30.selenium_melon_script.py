import time

from selenium import webdriver


options = webdriver.ChromeOptions()
options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36')

browser = webdriver.Chrome('./chromedriver.exe', options=options)

browser.get('https://www.melon.com/index.htm')
time.sleep(3)
# 뮤직어워드 링크를 클릭
browser.find_element_by_css_selector('#gnb_menu > ul:nth-child(1) > li.nth8 > a').click()
time.sleep(3)
browser.close()

