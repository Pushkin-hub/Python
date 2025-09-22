import requests
from bs4 import BeautifulSoup as bs
import json

response = requests.get('https://yandex.ru/pogoda/ru/krasnodar')

if response.status_code == 200:
    soup = bs(response.text)
    element = soup.select_one('')
else:
    print(f'Error. status_code {response.status_code}')

