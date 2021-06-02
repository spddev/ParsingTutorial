#pip install beautifulsoup4
from bs4 import BeautifulSoup

with open("blank/index2.html", encoding="utf-8") as file:
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

# user_name = soup.find("div", {"class": "user__name"}).find("span").text
# print(user_name)

# user_name = soup.find("div", {"class": "user__name", "id" : "aaa"}).find("span").text
# print(user_name)

# find_all_spans_in_user_info = soup.find(class_="user__info").find_all("span")
# print(find_all_spans_in_user_info)

# for item in find_all_spans_in_user_info:
    # print(item.text)

# print(find_all_spans_in_user_info[0])
# print(find_all_spans_in_user_info[2].text)

# social_links = soup.find(class_="social__networks").find(
#     "ul").find_all("a")
# print(social_links)

# all_a = soup.find_all("a")
# print(all_a)

# for item in all_a:
#     item_text = item.text
#     item_url = item.get("href")
#     # print(item_url)
#     print(f"{item_text} : {item_url}")

# .find_parent()  .find_parents()

# post_div = soup.find(class_="post__text").find_parent("div", "user__post")
# print(post_div)

# post_divs = soup.find(class_="post__text").findParents("div", "user__post")
# print(post_divs)

# .next_element   .previous_element
# next_el = soup.find(class_="post__title").next_element.next_element.text
# print(next_el)

# next_el = soup.find(class_="post__title").find_next().text
# print(next_el)

# .find_next_sibling()  .find_previous_sibling()
# next_sib = soup.find(class_="post__title").find_next_sibling()
# print(next_sib)

prev_sib = soup.find(class_="post__date").find_previous_sibling()
print(prev_sib)