#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-05-20

class Solution:

    def printListFromTailToHead(self,listNode):
        list = []
        while listNode:
            list.insert(0, listNode.val)
            listNode = listNode.next

        return list

    

