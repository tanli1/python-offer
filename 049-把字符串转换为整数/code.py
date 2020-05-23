#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-04-24

class Solution:
    def StrToInt(self, s):
        # write code here
        if s=='':
            return 0

        numlist=['0','1','2','3','4','5','6','7','8','9']
        sum=0
        flag2num = {'-':-1,'+':1}
        first = s[0]
        flag = 1
        if first in flag2num:
            flag = flag2num[first]
            for i in s[1:]:
                if i in numlist:
                    sum = sum * 10 + numlist.index(i)
                else:
                    sum = 0
                    break
        else:
            for i in s[0:]:
                if i in numlist:
                    sum = sum * 10 + numlist.index(i)
                else:
                    sum = 0
                    break

        if -0x7fffffff-1<=sum*flag <= 0x7fffffff:
            return sum * flag
        else:
            return 0

if __name__ =='__main__':
    target = 15
    array = '+123567890'
    answer = Solution()
    print(answer.StrToInt(array))




