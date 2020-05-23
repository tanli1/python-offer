#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-04-16

class Solution:
    def splitSpace(self,s):
        # 对空格split得到list，用'%20'连接（join）这个list
        return '%20'.join(s.split(' '))

if __name__ == '__main__':
    a = Solution()
    print(a.splitSpace('We are happy'))