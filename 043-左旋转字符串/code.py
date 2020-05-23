#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-04-22

class Solution:
	def LeftRotateString(self, s, n):
		return s[n:] + s[:n]

if __name__ =='__main__':
    answer = Solution()
    s1 = 'helloword.'
    print(answer.LeftRotateString(s1,5))