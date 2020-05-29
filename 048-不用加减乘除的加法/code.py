#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-05-29


class Solution:
    def add(self, n1, n2):
        sums = 0    # 保存不进位相加结果
        carry = 0   # 保存进位值
        while True:
            sums = n1 ^ n2           # 用异或代替不进位相加
            carry = (n1 & n2) << 1   # 与操作代替计算进位值
            n1 = sums
            n2 = carry
            if carry == 0:
                break
        return sums

if __name__ =='__main__':
    sum = Solution()
    print(sum.add(2,4))
