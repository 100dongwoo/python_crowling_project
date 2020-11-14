import requests
from bs4 import BeautifulSoup

res = requests.get('https://www.donga.com/news/Culture/article/all/20201113/103953508/1')
soup = BeautifulSoup(res.content, 'html.parser')
body = soup.find(class_='article_txt').findAll('div')
f = open('daum.txt', 'w')
# print(body)
article = [];
for i in body:
    article.append(i.get_text())
    print(i.get_text())
    f.write(i.get_text())
print(article)
f.close()
