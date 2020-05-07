# -*- coding: utf-8 -*-
# Created : 2020/3/18 16:54
# Author  : zhangguoqing
# E-mail  : zhangguoqing84@westlake.edu.cn
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json
import os
os.chdir(r"D:\Project\20191011-FunGene\抗生素抗性数据库\原始数据库\CARD-2020-03\card-data")
# model 列表
modellist = []
with open('modelIDlist.txt') as f:
    for line in f.readlines():
        if line != None:
            line = line.strip("\n")
            modellist.append(line)
print(modellist)
print("原modellist长度为：",len(modellist))


with open('card.json', encoding='utf-8') as f:

    line = f.readline()

    d = json.loads(line)
    print("card.json的model个数为：", len(d))
    for id in modellist:
        if id not in d:
            modellist.remove(id)
print(modellist)
print("去除不存在的model后modellist长度为：" , len(modellist))
cardkey = []
with open('card.json', encoding='utf-8') as f:

    line = f.readline()

    d = json.loads(line)
    for key in d.keys():
        cardkey.append(key)
print(cardkey)
