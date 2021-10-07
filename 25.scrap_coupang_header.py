import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
}



res = requests.get('https://www.coupang.com/np/campaigns/82/components/194176', headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
price_tag = soup.select_one('#productList > Li:nth-child(1) > a > dl > dd > div.price-area > div > div.price > em > strong')
# #\32 7613130 > a > dl > dd > div.price-area > div > div.price > em > strong
print(price_tag.text)
