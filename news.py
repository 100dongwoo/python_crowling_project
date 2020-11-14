# import requests
# from bs4 import BeautifulSoup
#
#
# res = requests.get('https://news.v.daum.net/v/20170615203441266')
# soup = BeautifulSoup(res.content, 'html.parser')
# title = soup.find('title')
# # print(title)
# body = soup.find(id='harmonyContainer').findAll('p')
# f = open('daum.txt', 'w')
# # print(body)
# article = [];
# for i in body:
#     article.append(i.get_text())
#     # print(i.get_text())
#     f.write(i.get_text())
#
# print(article)
# f.close()
import requests
from bs4 import BeautifulSoup


res = requests.get('https://www.donga.com/news/List/Culture')
soup = BeautifulSoup(res.content, 'html.parser')

# for link in soup.find(id="content").findAll("a"):
#     if 'href' in link.attrs:
#          print (link.attrs['href'])
# 되는거



# https://www.donga.com/news/Culture/List 리스트에 URL만 다가져오는거
array=[];
req=requests.get('https://www.donga.com/news/Culture/List')
soup2=BeautifulSoup(req.text,'html.parser')
for i in soup2.select("#content > div.articleList>div.thumb > a"):
    array.append(i['href'])
    # print(i['href'])
print(len(array))


# for i in soup2.find_all("span",class_="tit") :
#     print(i.text)


# body = soup.find(id='content').findAll("a")



# print(body)
#
# f = open('daum.txt', 'w')
# # print(body)
# article = [];
# for i in body:
#     article.append(i.get_text())
#     # print(i.get_text())
#     f.write(i.get_text())
#
# print(article)
# f.close()