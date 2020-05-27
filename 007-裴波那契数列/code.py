#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-05-27

class Solution:
    def Fibonacci(self, n):
        # write code here
        if n <= 1:
            return n
        first, second, third = 0, 1, 0
        for i in range(2, n+1):
            third = first + second
            first = second
            second = third
        return third

if __name__ =='__main__':
    answer = Solution()
    print(answer.Fibonacci(5))