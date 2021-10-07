import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}

res = requests.get('https://www.melon.com/chart/index.htm', headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
title_tag = soup.select_one('#lst50 > td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a')
print(title_tag['title'])

# 앨범 타이틀을 출력
album_title_tag = soup.select_one('#lst50 > td:nth-child(7) > div > div > div > a')
print(album_title_tag.text)