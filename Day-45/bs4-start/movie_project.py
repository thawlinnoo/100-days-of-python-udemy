import requests
from bs4 import BeautifulSoup

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(url)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")

movies_name = soup.find_all(name="h3", class_="title")
movie_list = []
for movie in movies_name:
    movie_list.append(movie.get_text())

print(movie_list[::-1])

with open("Day-45/bs4-start/movie_name.txt", "a") as file:
    for movie in movie_list[::-1]:
        file.write(f"{movie}\n")
