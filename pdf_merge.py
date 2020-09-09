# _*_ coding: UTF-8 _*_
#  pdf文件拆分程序
import PyPDF2
import math
import os

# 打开一个可读的pdf对象
filedir="./iplant"
filelist = os.listdir(filedir)

# 创建一个空白的pdf
pdfWriter = PyPDF2.PdfFileWriter()
totalpage=0
for file in filelist:
    filename = os.path.join(filedir, file)
    pdfReader = PyPDF2.PdfFileReader(filename, strict = False)
    # 获取pdf总页数 大小
    pdfnums = pdfReader.numPages

    #%%
    for i in range(pdfnums):
        pageObj = pdfReader.getPage(i)
        pdfWriter.addPage(pageObj)
    pdfWriter.addBookmark(file[4:-4], pagenum=totalpage, parent=None)  # add bookmark
    totalpage += pdfnums

with open('1.pdf', 'wb') as pdfOutputFile:
    pdfWriter.write(pdfOutputFile)

print("Done!")