# -*- coding: utf-8 -*-
# Created : 2020/5/7 16:40
# Author  : zhangguoqing
# E-mail  : zhangguoqing84@westlake.edu.cn
"""
问题描述：
给定一个正整数n, 找到若干个完全平方数(例如，1，4，9...)，使得它们的和等于n, 完全平方数的个数最少。
示例：n=12，返回3， 12 = 4+4+4
"""


class Solution:
    def numSquares(self, n):
        while n % 4 == 0:
            n //= 4
        if n % 8 == 7:
            return 4
        for i in range(n + 1):
            temp = i * i
            if temp <= n:
                if int((n - temp) ** 0.5) ** 2 + temp == n:
                    return 1 + (0 if temp == 0 else 1)
            else:
                break
        return 3

if __name__ == '__main__':
    n = 12
    print("初始值：", n)
    solution = Solution()
    print("结果： ", solution.numSquares(n))

