import requests
from bs4 import BeautifulSoup


URL = "https://news.naver.com/main/read.nhn?mode=LSD&mid=sec&sid1=102&oid=127&aid=0000030247"
res = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
soup = BeautifulSoup(res.text, 'html.parser')
body = soup.select("div._article_body_contents")
print(body)
f = open('daum.txt', 'w',encoding='utf-8')
for i in body:
        print(i.get_text())
        f.write(i.get_text())
f.close()
