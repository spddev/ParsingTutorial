# pip install bs4 requests lxml

import requests
from bs4 import BeautifulSoup

url = "http://www.health-diet.ru/table_calorie"

headers = {
    "Accept" : "*/*",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
}

req = requests.get(url, headers=headers)
src = req.text
print(src)