import requests
from bs4 import BeautifulSoup

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, 'html.parser')
movies_titles = soup.find_all(name="h3", class_="title")
name_of_movies = []
for i in range(len(movies_titles)-1, -1,-1):
    name_of_movies.append(movies_titles[i].getText())
print(name_of_movies)

with open("movies.txt", mode="w") as file:
    for movie in name_of_movies:
        file.write(f"{movie}\n")

