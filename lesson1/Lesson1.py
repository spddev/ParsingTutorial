#pip install beautifulsoup4
from bs4 import BeautifulSoup

with open("blank/index.html") as file:
    src = file.read()
# print(src)

soup = BeautifulSoup(src, "lxml")

title = soup.title
# print(title)
# print(title.text)
# print(title.string)

# .find() .find_all()
# page_h1 = soup.find("h1")
# print(page_h1)

# page_all_h1 = soup.find_all("h1")
# print(page_all_h1)

# for item in page_all_h1:
#     print(item.text)

# user_name = soup.find("div", class_="user__name")
# print(user_name.text.strip())

user_name = soup.find("div", {"class": "user__name"}).find("span").text
print(user_name)