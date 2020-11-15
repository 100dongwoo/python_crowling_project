import requests
from bs4 import BeautifulSoup
# 한겨레
urlArray = []  # list페이지 url (1~10페이지까지)
new_URL = []  # urlArray에 있는 new기사별 array
DongaUrl = "http://www.hani.co.kr/arti/culture/culture_general/home01.html"  # Only 동아일보
plusDongaUrl = "https://www.donga.com/news/Culture/List?ymd=&m=NP"  # 동아일보에 다른기사들 포함(몇 가지)

# 넥스트 a 만 가져와서 제목만 따오는거
req = requests.get(DongaUrl)
soup = BeautifulSoup(req.text, 'html.parser')

for i in soup.select("div.paginate > a"):
    urlArray.append("http://www.hani.co.kr" + i['href'])
    print("http://www.hani.co.kr"+ i['href'])
# 동아일보 특성상 문화 페이지에도 다른 종류에 기사들이 포함되있다.
# for UrlList in urlArray:
#     req2 = requests.get(UrlList)
#     soup2 = BeautifulSoup(req2.text, 'html.parser')
#     for i in soup2.select("span.article-photo> a"):
#         new_URL.append("http://www.hani.co.kr"+i['href'])
#         print("http://www.hani.co.kr"+i['href'])

# -------------------내용------------------------------------------------
# f = open('daum.txt', 'w')
# for postURL in new_URL:
#     # print(postURL)
#     res4 = requests.get(postURL)
#     soup4 = BeautifulSoup(res4.text, 'html.parser')
#     body = soup4.find(class_='article-text-font-size').find(class_="text")
#     print(body)
#     # for i in body:
#     #     print(i.get_text())
#         # f.write(i.get_text())
# f.close()

# ------------------------------------------------------------------
