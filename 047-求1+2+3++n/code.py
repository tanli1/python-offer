#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-05-29

class Solution:
    def sumTest(self,n):
        sum = 0
        while n > 0:
            sum = sum + n
            n -= 1
        return sum 

if __name__ =='__main__':
    sum = Solution()
    print(sum.sumTest(5))