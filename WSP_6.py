import requests
from bs4 import BeautifulSoup
import lxml as lxml

website = 'https://subslikescript.com/movie/Humanoids_The_Real_Close_Encounters_of_the_Third_Kind_2022-11102198'
content = requests.get(website)
t_file = content.text
soup = BeautifulSoup(t_file,'lxml')
#print(soup)

box = soup.find("article",class_ = "main-article")
head = box.find("h1").get_text()
transcript = box.find("div",class_ ="full-script").get_text(strip = True,separator = '')

with open('humonoid.txt','w',encoding="utf-8") as file:
    file.write(transcript)




