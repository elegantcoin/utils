# -*- coding: utf-8 -*-
import os

"""
合并多个txt
"""

# 获取目标文件夹的路径
path = 'C:\\Users\\Sword\\PycharmProjects\\sgm\\txt\\'
# 获取当前文件夹中的文件名称列表
filenames = os.listdir(path)
result = "merge.txt"
# 打开当前目录下的result.txt文件，如果没有则创建
file = open(result, 'w+', encoding="utf-8-sig")
# 向文件中写入字符

# 先遍历文件名
for filename in filenames:
    try:
        filepath = path +filename
        # 遍历单个文件，读取行数
        for line in open(filepath, encoding="utf-8"):
            file.writelines(line)
        file.write('\n')
    except Exception as e:
        print(e, "Error:", filepath)
        continue

# 关闭文件
file.close()