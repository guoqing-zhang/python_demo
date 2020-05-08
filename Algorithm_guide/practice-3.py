# -*- coding: utf-8 -*-
# Created : 2020/5/8 8:34
# Author  : zhangguoqing
# E-mail  : zhangguoqing84@westlake.edu.cn
"""
问题面熟：
实现 int sqrt(int x)函数，计算并返回x的平方根。
示例：
sqrt(3)=1; sqrt(4)=2; sqrt(5)=2; sqrt(10) = 3
"""

# 参数x是一个整数
# 返回值是x的平方根
class Solution:
    def sqrt(self, x):
        l, r = 0, x
        while l + 1 < r:
            m = (r + 1) // 2
            if m * m == x:
                return m
            elif m * m > x:
                r = m
            else:
                l = m
        if l * l == x:
            return l
        if r * r == x:
            return r
        return l


if __name__ == '__main__':
    temp = Solution()
    x1 = 5
    x2 = 10
    print(("输入： " + str(x1)))
    print(("输出： " + str(temp.sqrt(x1))))
    print(("输入： " + str(x2)))
    print(("输出： " + str(temp.sqrt(x2))))