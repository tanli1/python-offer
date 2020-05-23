#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-04-22

class Solution:
    def ReverseSentence(self, s): 
        a = s.split(" ")
        if len(a) == 1:
            return s
        return a[-1] + " " + self.reverse(list(a[:-1]), 0, len(a)-2)

    def reverse(self,s,low,high):
        while low < high:
            s[low],s[high] = s[high],s[low]
            low += 1
            high -= 1
        print 's = ',s
        print ' '.join(s)
        return ' '.join(s)

if __name__ =='__main__':
    answer = Solution()
    s1 = "I am a student."
    print(answer.ReverseSentence(s1))
