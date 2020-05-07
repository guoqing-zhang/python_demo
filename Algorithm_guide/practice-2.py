# -*- coding: utf-8 -*-
# Created : 2020/5/7 19:05
# Author  : zhangguoqing
# E-mail  : zhangguoqing84@westlake.edu.cn
"""
问题描述：
检测一个整数是否为2的幂次
示例：
n=4，返回True；n=5，返回False。
"""

# 参数n是一个整数
# 返回True或者False

class Solution:
    def checkPower0f2(self, n):
        ans = 1
        for i in range(31):
            if ans == n:
                return True
            ans = ans << 1 #[1,2,4,8,16]
            # 2^30以内均可检查
        return False

if __name__ == '__mian__':
    temp = Solution()
    nums1 = 16
    nums2 = 17
    print(("输入： " + str(nums1)))
    print(("输入： " + str(temp.checkPower0f2(nums1))))
    print(("输入： " + str(nums2)))
    print(("输入： " + str(temp.checkPower0f2(nums2))))