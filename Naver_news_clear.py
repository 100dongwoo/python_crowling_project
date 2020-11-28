import requests
from bs4 import BeautifulSoup
from urllib import parse

urlArray = []  # list페이지 url (1~10페이지까지)
new_URL = []  # urlArray에 있는 new기사별 array
checkURL = "https://news.naver.com/"
keyword = input('원하시는 검색단어를 검색하세욘')
parse.quote(keyword)
NaverNews = f"https://search.naver.com/search.naver?&where=news&query={parse.quote(keyword)}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=41&start=1"
req = requests.get(NaverNews)
soup = BeautifulSoup(req.text, 'html.parser')
maxCount = 100;  # 원하는 크롤링 기사 수
url = ''
isMax = False
print(NaverNews)

while 1:
        if isMax:
            break
        for i in soup.select(".btn_next"):
            if isMax:
                break
            if len(new_URL) == 0:
                url = NaverNews
            else:
                print("https://search.naver.com/search.naver" + i['href'])
                url = ("https://search.naver.com/search.naver" + i['href'])
            req = requests.get(url)
            soup = BeautifulSoup(req.text, 'html.parser')
            for i in soup.select(".news_area a.info"):
                if i['href'][:len(checkURL)] == checkURL:
                    print(i['href'])
                    new_URL.append(i['href'])
                    if len(new_URL) >= int(maxCount):
                        isMax = True
                        break
print(len(new_URL))
