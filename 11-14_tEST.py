import requests
from bs4 import BeautifulSoup

urlArray = []  # list페이지 url (1~10페이지까지)
new_URL = []  # urlArray에 있는 new기사별 array
DongaUrl = "https://www.donga.com/news/Culture/List?ymd=&m=NP"  # Only 동아일보
plusDongaUrl = "https://www.donga.com/news/Culture/List"  # 동아일보에 다른기사들 포함(몇 가지)

# 넥스트 a 만 가져와서 제목만 따오는거
req = requests.get(DongaUrl)
soup2 = BeautifulSoup(req.text, 'html.parser')
for i in soup2.select("#content > div.page > a"):
    urlArray.append(DongaUrl + i['href'])
    # print("https://www.donga.com/news/Culture/List" + i['href'])

# list에있는 기사url을가져온다=> 동아일보만 200개 , PLUS동아일보는 193개
# 동아일보 특성상 문화 페이지에도 다른 종류에 기사들이 포함되있다.
for i in range(0, len(urlArray) - 1):
    req = requests.get(urlArray[i])
    soup2 = BeautifulSoup(req.text, 'html.parser')
    for i in soup2.select("#content > div.articleList>div.thumb > a"):
        new_URL.append(i['href'])
        # print(i['href'])
print(len(new_URL))

# ----------------------------------------------------------------------------
f = open('daum.txt', 'w')
for postURL in new_URL:
    res=requests.get(postURL)
    soup=BeautifulSoup(res.content,'html.parser')
    body = soup.find(class_='article_txt').findAll('div')
    # print(body)
    article = [];
    for i in body:
        article.append(i.get_text())
        # print(i.get_text())
        f.write(i.get_text())
f.close()
# ------------------------------------------------------------------

# https://www.donga.com/news/Culture/List 리스트에 URL만 다가져오는거
array = [];
req = requests.get('https://www.donga.com/news/Culture/List')
soup2 = BeautifulSoup(req.text, 'html.parser')

for i in soup2.select("#content > div.articleList>div.thumb > a"):
    array.append(i['href'])
    # print(i['href'])
