from bs4 import BeautifulSoup
import os
import requests
os.chdir("./day45")
URL = "https://www.empireonline.com/movies/features/best-movies-2"
URL2 ="https://www.empireonline.com/tv/features/best-tv-shows-ever-2/"



response1 = requests.get(URL)
#response2 = requests.get(URL2)

website1_html = response1.text
#website2_html = response2.text

soup1 = BeautifulSoup(website1_html, "html.parser")
with open("testo.txt", "w") as file:
    file.write(soup1.prettify()) 
#soup2 = BeautifulSoup(website2_html, "html.parser")
#print (soup1.prettify())
#all_movies = soup1.find_all(name="h3")
#all_series = soup2.find_all(name = "h3", class_= "jsx-4245974604")
#print (all_movies)
#movie_titles = [movie.getText() for movie in all_movies]
#serie_titles = [serie.getText() for serie in all_series]

#movies = movie_titles[::-1]
#series = serie_titles[::-1]
#print (movies)
#print (series)

