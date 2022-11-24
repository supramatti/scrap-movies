import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

contents = requests.get(URL)
contents.raise_for_status()
contents = contents.text
soup = BeautifulSoup(contents, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movies = []

for movie in all_movies:
    movies.append(movie.getText())

movies.reverse()

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(movie)
        file.write("\n")

