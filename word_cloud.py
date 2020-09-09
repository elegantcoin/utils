#fc-list :lang=zh 
# _*_ coding: UTF-8 _*_
from wordcloud import WordCloud
import jieba
from matplotlib import pyplot as plt
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-f","--file-name",required=True,
		help="Input file name")
args=vars(ap.parse_args())
outname=args["file_name"].split(".")

fig,ax=plt.subplots()

stopwords = [line.strip() for line in  open('./src/stopwords.txt',encoding='UTF-8-sig').readlines()]

with open(args["file_name"],'rb') as f:
    text=f.read()

wsplit=jieba.cut(text)
words="".join(wsplit)

# font_path=r'./usr/share/fonts/wqy-microhei/wqy-microhei.ttc',
mycloudword=WordCloud(font_path='C:\Windows\Fonts\MSYH.ttc',
                      width=1280, 
                      height=960, 
                      scale=1, 
                      margin=2,
                      background_color='white',
                      relative_scaling=0.5,
                      max_words=10000, 
                      min_font_size=10, 
                      max_font_size=200,
                      stopwords=stopwords, 
                      random_state=50).generate(words)

mycloudword.to_file(outname[0]+'_result'+'.png')
ax.imshow(mycloudword)
ax.axis("off")
plt.show()

