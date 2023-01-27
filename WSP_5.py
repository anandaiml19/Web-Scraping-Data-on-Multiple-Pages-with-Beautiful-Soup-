import requests
from bs4 import BeautifulSoup
import lxml as lxml

website = 'https://subslikescript.com/movie/Boys_Feels_Stand_by_Me-23596610'
content = requests.get(website)
t_file = content.text
soup = BeautifulSoup(t_file,'lxml')
#print(soup)

box = soup.find("article",class_ = "main-article")
head = box.find("h1").get_text()
transcript = box.find("div",class_ ="full-script").get_text(strip = True,separator = '')

with open('boy.txt','w',encoding="utf-8") as file:
    file.write(transcript)




