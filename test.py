# from turtle import goto
#
# import requests
# from bs4 import BeautifulSoup
# from urllib import parse
#
# urlArray = []  # list페이지 url (1~10페이지까지)
# new_URL = []  # urlArray에 있는 new기사별 array
# keyword = "국제"
# checkURL="https://news.naver.com/"
# parse.quote(keyword)
# NaverNews = f"https://search.naver.com/search.naver?&where=news&query={parse.quote(keyword)}{parse.quote('+네이버뉴스')}&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=41&start=1"
# print(NaverNews)
# req = requests.get(NaverNews)
# soup = BeautifulSoup(req.text, 'html.parser')
# maxCount=100;
# count=0;
# url=''
# while 1:
#     for i in soup.select(".sc_page_inner a"):
#         # print("https://search.naver.com/search.naver" + i['href'])
#         urlArray.append("https://search.naver.com/search.naver" + i['href'])
#     for UrlList in urlArray:
#         req2 = requests.get(UrlList)
#         soup2 = BeautifulSoup(req2.text, 'html.parser')
#         for i in soup2.select(".news_area a.info"):
#             if i['href'][:len(checkURL)] == checkURL:
#                 print(i['href'])
#                 new_URL.append(i['href'])
#                 if len(new_URL) >= int(maxCount):
#                     goto ONE;
#     for i in soup.select(".btn_next"):
#         print("https://search.naver.com/search.naver" + i['href'])
#         url=("https://search.naver.com/search.naver" + i['href'])
#         req = requests.get(url)
#         soup = BeautifulSoup(req.text, 'html.parser')
#
# ONE:
#     printf("1을 입력하셨습니다! \n");
#     goto END;
#
# # # 위 for문에서 가져온 url을 통해 그 url에있는 기사들에 url을 가져옴
# #     for UrlList in urlArray:
# #         req2 = requests.get(UrlList)
# #         soup2 = BeautifulSoup(req2.text, 'html.parser')
# #         for i in soup2.select(".news_area a.info"):
# #             if i['href'][:len(checkURL)] == checkURL:
# #                 print(i['href'])
# #                 new_URL.append(i['href'])
# print(len(new_URL))
#
#
#
#
#
#
#
#
# # for i in soup.select(".btn_next"):
# #     print("https://search.naver.com/search.naver"+i['href'])
# #     urlArray.append("https://search.naver.com/search.naver"+i['href'])
#
#
#
#
#
# # 위 URL에서 paging url 가져오는 반복문
# # # btn_next
# # for i in soup.select(".btn_next"):
# #     print("https://search.naver.com/search.naver"+i['href'])
# #     urlArray.append("https://search.naver.com/search.naver"+i['href'])
#
# # req = requests.get(NaverNews)
# # soup = BeautifulSoup(req.text, 'html.parser')
# # # 위 URL에서 paging url 가져오는 반복문
# #
#
# #
# #
# # # 위 for문에서 가져온 url을 통해 그 url에있는 기사들에 url을 가져옴
# # for UrlList in urlArray:
# #     req2 = requests.get(UrlList)
# #     soup2 = BeautifulSoup(req2.text, 'html.parser')
# #     for i in soup2.select(".news_tit"):
# #         print(i['href'])
# #         new_URL.append(i['href'])
# # print(len(new_URL))
# # ////////////////////////////////////
#
#
# # req2 = requests.get("https://search.naver.com/search.naver?&where=news&query=%EA%B5%AD%EC%A0%9C&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=66&start=91")
# # soup2 = BeautifulSoup(req2.text, 'html.parser')
# # for i in soup2.select(".news_tit"):
# #     # print(i)
# #     print(i['href'])
# #     new_URL.append(i['href'])
#
#
# # f = open('daum.txt', 'w')
# # for postURL in new_URL:
# #     try:
# #         res4 = requests.get(postURL)
# #         soup4 = BeautifulSoup(res4.text, 'html.parser')
# #         body = soup4.find(id='mArticle').findAll("p")
# #         for i in body:
# #             # if i.get_text()[:len("\n<저작권자(c) 연합뉴스,\n무단 전재-재배포 금지>")] != "\n<저작권자(c) 연합뉴스,\n무단 전재-재배포 금지>":
# #             print(i.get_text())
# #             f.write(i.get_text() + "\n")
# #     except Exception as e:
# #         print(e)
# #         pass
# # f.close()
#
# # /////////////////////////////////////////////////////////////////////////////////////
