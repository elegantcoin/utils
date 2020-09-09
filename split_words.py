# 原文：https://blog.csdn.net/jiasudu1234/article/details/70065917 
# _*_ coding: UTF-8 _*_
import csv
import jieba
import jieba.posseg as psg
import copy
import time
import argparse


ap=argparse.ArgumentParser()
ap.add_argument("-f","--file-name",required=True,
		help="Input file name")
args=vars(ap.parse_args())

#读取停词表
stopwords = [line.strip() for line in  open('./src/stopwords.txt',encoding='UTF-8-sig').readlines()]
stopflags=["m","o","q","w","x","y"]
#一行行读取csv
file_object2=open(args["file_name"],'r',encoding ='UTF-8-sig').read().split('\n')

#建立分词存储列表
Rs1=[]
Rs2=[] 
#统计词频的字典
dic={}
dic2= {"Ag":"形语素","a":"形容词","ad":"副形词","an":"名形词","b":"区别词","c":"连词","dg":"副语素","d":"副词","e":"叹词","f":"方位词","g":"语素",\
    "h":"前接成分","i":"成语","j":"简称略语","k":"后接成分","l":"习用语","m":"数词","Ng":"名语素","n":"名词","nr":"人名","ns":"地名","nt":"机构团体",\
    "nz":"其他专名","o":"拟声词","p":"介词","q":"量词","r":"代词","s":"处所词","tg":"时语素","t":"时间词","u":"助词","vg":"动语素","v":"动词",\
    "vd":"副动词","vn":"名动词","w":"标点符号","x":"非语素字","y":"语气词","z":"状态词","un":"未知词",}

for i in range(len(file_object2)):
	result=[]
	# 选择cut的模式
	# seg_list = jieba.cut(file_object2[i])
	seg_list = psg.cut(file_object2[i])
	# seg_list = jieba.cut_for_search(file_object2[i])
	#添加源数据列	
	# result.append(file_object2[i])
	#读取每一行分词	
	for w in seg_list :
		if w.word not in stopwords and w.flag not in stopflags:
			result.append(w.word)
			dic[w]=dic.get(w,0)+1
			continue
	#把分词写入源列表后面	
	Rs1.append(result)

#写入CSV,并用时间命名文件 避免重名
# 08 05 2019 09:49:02 时间格式
doctime=str(time.strftime("%m %d %Y %H:%M:%S", time.localtime()))
mon=doctime[0:2]
dy=doctime[3:5]
yr=doctime[6:10]
hr=doctime[11:13]
mi=doctime[14:16]
se=doctime[17:19]

file=open('0fenci_'+yr[-2:]+mon+dy+'_'+hr+'_'+mi+se+'.csv','w',newline='',encoding='utf-8-sig')
writer = csv.writer(file)
writer.writerows(Rs1)
file.close() 

# dic排序
dic1=copy.deepcopy(dic)
dic = sorted(dic1.items(), key=lambda d:d[1], reverse = True)
for k,v in enumerate(dic):
	Rs2.append((v[0].word,v[0].flag,dic2.get(v[0].flag),v[1]))

# for k,v in enumerate(dic):
# 	Rs2.append((v,dic[v]))

#print(Rs2[:10])
file=open('1keyword_'+yr[-2:]+mon+dy+'_'+hr+'_'+mi+se+'.csv','w',newline='',encoding='utf-8-sig')
writer = csv.writer(file)
writer.writerows(Rs2)
file.close() 
