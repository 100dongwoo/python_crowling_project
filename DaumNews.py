import requests
from bs4 import BeautifulSoup
urlArray = []  # list페이지 url (1~10페이지까지)
new_URL = []  # urlArray에 있는 new기사별 array
DaumUrl = "https://news.daum.net/breakingnews/culture"
req = requests.get(DaumUrl)
soup = BeautifulSoup(req.text, 'html.parser')
# 위 URL에서 paging url 가져오는 반복문
for i in soup.select(".paging_news>span>a"):
    # print("https://news.daum.net" + i['href'])
    urlArray.append("https://news.daum.net" + i['href'])

# 위 for문에서 가져온 url을 통해 그 url에있는 기사들에 url을 가져옴
for UrlList in urlArray:
    req2 = requests.get(UrlList)
    soup2 = BeautifulSoup(req2.text, 'html.parser')
    for i in soup2.select("ul.list_news2.list_allnews>li>a"):
        print(i['href'])
        new_URL.append(i['href'])

f = open('daum.txt', 'w')
for postURL in new_URL:
    try:
        res4 = requests.get(postURL)
        soup4 = BeautifulSoup(res4.text, 'html.parser')
        body = soup4.find(id='mArticle').findAll("p")
        for i in body:
            # if i.get_text()[:len("\n<저작권자(c) 연합뉴스,\n무단 전재-재배포 금지>")] != "\n<저작권자(c) 연합뉴스,\n무단 전재-재배포 금지>":
            print(i.get_text())
            f.write(i.get_text() + "\n")
    except Exception as e:
        print(e)
        pass
f.close()

# /////////////////////////////////////////////////////////////////////////////////////