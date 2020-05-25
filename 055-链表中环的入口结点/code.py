#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-05-25

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FirstNodeLoop(self, pHead):
        tmpNode = []
        p = pHead
        while p:
            if p in tmpNode:
                return p
            else:
                tmpNode.append(p)
            p = p.next
        
        return None