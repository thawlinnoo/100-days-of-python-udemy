from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")

titles = soup.find_all(name="span", class_="titleline")
titles_upvote = soup.find_all(name="span", class_="score")




title_text_list = []
title_link_list = []
title_upvote_list = []

for title in titles:
    title_text = title.a.get_text()
    title_link = title.a.get("href")
    title_text_list.append(title_text)
    title_link_list.append(title_link)

for title in titles_upvote:
    title_upvote = title.get_text()
    title_upvote_list.append(title_upvote.split()[0])

max_score = max(title_upvote_list)
max_index = title_upvote_list.index(max_score)

print(title_text_list[max_index])
print(title_link_list[max_index])

    

# for title in range(len(title_text_list)):
#     print(title_text_list[title])
#     print(title_link_list[title])
#     print(title_upvote_list[title])
#     print(" ")






# for title in titles:
#     print(title.get_text())



# with open("Day-45/bs4-start/website.html", "r") as file:
#     content = file.read()

# soup = BeautifulSoup(content, "html.parser")
# # print(soup.title.string)

# li_tags = soup.find_all(name="li")
# for tag in li_tags:
#     print(tag.get_text())
#     print(tag.get("href"))getText()

# heading = soup.find(name="h1", id="name")
# print(heading)

# heading = soup.find(name="h1", class_="name") #"need _ to take class"
# print(heading)

# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(selector=".heading")
# print(headings)

