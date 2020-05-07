# -*- coding: utf-8 -*-
# Created : 2019/12/19 9:14

# Author  : zhangguoqing

# E-mail  : zhangguoqing84@westlake.edu.cn
import math

# 温度转换
f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('{:.1f}华氏度 = {:.1f}摄氏度'.format(f,c)) #format格式

# 输入半径计算圆的周长和面积

radius = float(input('请输入圆的半径： '))
perimeter = 2 * math.pi * radius
area = math.pi * radius * radius
print('周长：{:.2f}'.format(perimeter))
print('面积：{:.2f}'.format(area))

# 输入年份判断闰年
year = int(input('请输入年份：'))
is_leap = (year % 4 == 0 and year % 100 != 0) or \
           year % 400 == 0
print(is_leap)