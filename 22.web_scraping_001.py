import requests
import json

res = requests.get('https://music.bugs.co.kr/chart')

print(res.json())

