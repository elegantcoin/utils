# _*_ coding: UTF-8 _*_
#  pdf文件拆分程序
import PyPDF2
import math
import os

# 打开一个可读的pdf对象
filename="X86指令集体系结构：全面的32位和64位覆盖率"

pdfReader = PyPDF2.PdfFileReader(filename+'.pdf', strict = False)
# 获取pdf总页数 大小
pdfnums = pdfReader.numPages
size = os.path.getsize(filename+'.pdf')
num = math.ceil(size/(9.5*1024*1024))
n = pdfnums//num +1
if n>=300:
    n = 300


#%%
# 将总页码循环到一个列表中
pagenum_list = list(range(pdfnums))

# 将总页码按照指定的个数分为多个小列表
page_list = [pagenum_list[i:i + n] for i in range(0, len(pagenum_list), n)]

for i in range(len(page_list)):
    # 创建一个空白的pdf
    pdfWriter = PyPDF2.PdfFileWriter()
    # 提取指定页面
    for pageNum in range(page_list[i][0], page_list[i][-1] + 1):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)

    with open('1'+filename[:5]+'_%s' % i + '.pdf', 'wb') as pdfOutputFile:
        pdfWriter.write(pdfOutputFile)

print("Done!")