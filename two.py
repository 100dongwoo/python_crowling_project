import time

import requests
from bs4 import BeautifulSoup
# 한겨레
from pip._internal.models import link

urlArray = []  # list페이지 url (1~10페이지까지)
new_URL = []  # urlArray에 있는 new기사별 array
DongaUrl = "https://www.yna.co.kr/culture/performance-exhibition?site=navi_culture_depth02"  # Only 동아일보
# 넥스트 a 만 가져와서 제목만 따오는거
req = requests.get(DongaUrl)
soup = BeautifulSoup(req.text, 'html.parser')

for i in soup.select(".paging>a"):
    urlArray.append("https:" + i['href'])
    print("https:" + i['href'])


# 동아일보 특성상 문화 페이지에도 다른 종류에 기사들이 포함되있다.
for UrlList in urlArray:
    req2 = requests.get(UrlList)
    soup2 = BeautifulSoup(req2.text, 'html.parser')
    for i in soup2.select(".news-con> a"):
        new_URL.append("https:" + i['href'])
        # print("https:"+i['href'])

# -------------------내용------------------------------------------------
f = open('daum.txt', 'w')
for postURL in new_URL:
    try:
        res4 = requests.get(postURL)
        soup4 = BeautifulSoup(res4.text, 'html.parser')
        body = soup4.find(class_='story-news article').findAll("p")
        for i in body:
            if i.get_text()[:len("\n<저작권자(c) 연합뉴스,\n무단 전재-재배포 금지>")] != "\n<저작권자(c) 연합뉴스,\n무단 전재-재배포 금지>":
                 print(i.get_text())
                 f.write(i.get_text()+"\n")
    except Exception as e:
        print(e)
        pass
f.close()

# ------------------------------------------------------------------
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
