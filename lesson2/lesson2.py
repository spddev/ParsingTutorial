# pip install bs4 requests lxml

import requests
from bs4 import BeautifulSoup
import json
import csv
# url = "http://www.health-diet.ru/table_calorie"
#
# headers = {
#     "Accept" : "*/*",
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0"
# }
#
# req = requests.get(url, headers=headers)
# src = req.text
# # print(src)
#
# with open("index.html", "w", encoding="utf-8") as file:
#     file.write(src)

with open("index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_categories_dict = {}
all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")
for item in all_products_hrefs:
    item_text = item.text
    item_href = "http://www.health-diet.ru" + item.get("href")
    # print(f"{item_text}:{item_href}")

    all_categories_dict[item_text] = item_href
    # print(all_categories_dict)
# Сохранение данных в JSON-файл
with open("all_categories_dict.json", "w", encoding="utf-8") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)