#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-05-27

class Solution:
    def jumpFloorII(self, number):
        return 2 ** (munber-1)

        # if number <= 2:
        #     return number
        # total = 1
        # for _ in range(1, number): # _ 可以换成任何字符，下面用不到
        #     total *= 2
        # return total

if __name__ =='__main__':
    answer = Solution()
    print(answer.jumpFloorII(5))