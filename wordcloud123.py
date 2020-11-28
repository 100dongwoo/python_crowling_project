from wordcloud import WordCloud, STOPWORDS
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt

data1 = open('daum.txt', 'r', encoding='utf-8')
data2 = data1.read()

data1.close()
spwords = set(STOPWORDS)
spwords.add('손편지')
# spwords.add('때')

wc = WordCloud(font_path='C:/Windows/Fonts/H2GTRM.TTF', background_color='black', width=500, height=500, max_words=20,
               max_font_size=100)

okt = Okt()
noun = okt.nouns(data2)
count = Counter(noun)

noun_list = count.most_common()
for v in noun_list:
    print(v)

print(dict(noun_list))
wc.generate_from_frequencies(dict(noun_list))
wc.to_file('./wc.png')
plt.figure(figsize=(10, 8))
plt.imshow(wc)
plt.axis('off')
plt.show()
