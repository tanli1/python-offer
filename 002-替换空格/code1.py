#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-04-16


class Solution:
	# 用python字符串的replace方法
	def replaceSpace(self,s):
		return s.replace(' ','%20')  # string的replace方法，需要注意replace不会改变原string的内容
		                             # return s 返回的值是旧的字符串的值

if __name__ == '__main__':
    a = Solution()
    print(a.replaceSpace('We are happy'))