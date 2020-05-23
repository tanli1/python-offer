#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-04-16

class Solution:
    def replaceSpace(self,s):
        # 由于替换空格后，字符串长度需要增大。先扫描空格个数，计算字符串应有的长度，从后向前一个个字符复制（需要两个指针）。这样避免了替换空格后，需要移动的操作
        num_space = 0
        for i in s:
            if i == ' ':
                num_space += 1

        new_length = len(s) + num_space * 2
        index_orgin = len(s) -1
        index_new = new_length -1
        
        new_string = [None for i in range(new_length)]  # 把new_length 中都写None填充

        while index_orgin >= 0 & (index_new > index_orgin):
        	if s[index_orgin] == ' ':
        		new_string[index_new] = '0'
        		index_new -= 1
        		new_string[index_new] = '2'
        		index_new -= 1
        		new_string[index_new] = '%'
        		index_new -= 1
        	else:
        		new_string[index_new] = s[index_orgin]
        		index_new -= 1

        	index_orgin -= 1

        return ''.join(new_string)  # list中的数据连接在一起

if __name__ == '__main__':
    a = Solution()
    print(a.replaceSpace('We are happy'))