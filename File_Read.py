import sys
import requests
from bs4 import BeautifulSoup

data1 = open('./url.txt', 'r', encoding='utf-8')
data2 = data1.read()
array = []
# print(len(data2.split('\n')))
data3 = data2.split('\n')
for i in range(0, len(data2.split('\n'))):
    array.append(data3[i])

# print(array)
for i in range(0, len(array)):
    res = requests.get(array[i])
    soup = BeautifulSoup(res.content, 'html.parser')
    title = soup.find('title')
    print(title)
    with open('title.txt', 'a', encoding='utf-8') as f:
      for line in title:
         f.write(line + '\n')
