#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-04-19


def helper(s):
    if len(s) == 1:
        return s[0]

    res = []
    for i in range(len(s)):
        l = helper(s[:i] + s[i+1:])
        #print 'i ====',i
        #print (s[:i] + s[i+1:])
        #print 's= ',s
        #print 'l === ',l
        for j in l:
            #print 'j === ',j
            res.append(s[i] + j)
            #print 'helper res === ',res
    return res

def Permutation(ss):
    # write code here
    if not ss: 
        return []
    words = list(ss)   # 把字符串每个字母切割成list格式保存

    return list(sorted(set(helper(words))))   # = return helper(words) 额，进行了排序
    

print(Permutation('abc'))

