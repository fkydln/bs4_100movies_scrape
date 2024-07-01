import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
eo_website = response.text

soup = BeautifulSoup(eo_website, "html.parser")

# print(soup.title)

titles = soup.find_all("h3", class_="listicleItem_listicle-item__title__BfenH")
titles_list = []
for title in titles:
    titles_list.append(title.getText())

reversed_list = titles_list[::-1]
print(reversed_list)


with open("top100_movies.txt", "w") as file:
    for item in reversed_list:
        file.write(item + '\n')