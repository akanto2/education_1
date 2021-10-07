import requests
from bs4 import BeautifulSoup
import pandas as pd


def save_to_excel(list_of_list):
    df = pd.DataFrame(list_of_list)
    df.to_excel('coupang_rocket.xlsx', index=False, header=['물품명', '가격', '좋아요수', '이미지 URL'])
    print('excel save completed..')


def get_header():
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'
    }


def save_image_to(url):
    res = requests.get(url)
    with open('./images/' + url.split('/')[-1], 'wb') as f:
        f.write(res.content)


def main():
    page_url = 'https://www.coupang.com/np/campaigns/82/components/194176?page=2'
    res = requests.get(page_url, headers=get_header())
    soup = BeautifulSoup(res.text, 'html.parser')

    lists = soup.select('#productList > li')

    products = []

    for li in lists:
        image_url = 'https:' + li.select_one('a > dl > dt > img')['src']
        products.append([
        li.select_one('a > dl > dd > div.name').text.strip(),
        int(li.select_one('a > dl > dd > div.price-area > div > div.price > em > strong').text.replace(',', '')),
        int(li.select_one('a > dl > dd > div.other-info > div > span.rating-total-count').text[1:-1]),
        image_url
        ])
        save_image_to(image_url)

    save_to_excel(products)


if __name__ == '__main__':
    main()
