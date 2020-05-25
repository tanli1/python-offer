#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-05-25

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        if pHead1 == None or pHead2 == None:
            return None
        P1 = pHead1
        while p1:
            p2 = pHead2
            while p2:
                if p1 = p2:
                    return p1
                p2 = p2.next
            p1 = p1.next
        return None