#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-04-21

class Solution:
	def FirstNotRepeatingChar(self, s):
		if not s or len(s)>10000:
			return -1
		else:
			for i in s:
				if s.count(i) == 1:
					return s.index(i)  # 如果包含子字符串返回开始的索引值，否则抛出异常。
					#return s.find(i)   # 如果包含子字符串返回开始的索引值，否则返回-1。不影响后面程序执行

if __name__ =='__main__':
    answer = Solution()
    s1 = 'abcdefghiabcdegfg'
    print(answer.FirstNotRepeatingChar(s1))