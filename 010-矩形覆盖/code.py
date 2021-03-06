#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-05-27

class Solution:
    def rectCover(self, number):
        if number <= 2:
            return number
        first ,second, third = 1, 2, 0
        for i in range(3, number+1):
            third = first + second
            first = second
            second = third
        return third