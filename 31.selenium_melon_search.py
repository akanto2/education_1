import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36')
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

browser = webdriver.Chrome('./chromedriver.exe', options=options)

browser.get('https://www.melon.com/index.htm')
time.sleep(1)

browser.find_element_by_css_selector('#top_search').send_keys('아이유', Keys.ENTER)
time.sleep(1)
browser.get_screenshot_as_file('./screenshot.png')

soup = BeautifulSoup(browser.page_source, 'html.parser')
browser.close()

the_tag = soup.select_one('#frm_searchArtist > div > table > tbody > tr:nth-child(1) > td:nth-child(3) > div > div > a.fc_gray')

print(the_tag)
