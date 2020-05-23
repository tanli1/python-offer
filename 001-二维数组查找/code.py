#!/usr/bin/env python
# coding:utf-8
# Author: ltan
# Date: 2020-04-16

class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        # 选右上角的值和target做比较，往左下方移动
        rows = len(arry)          
        cols = len(arry[0])
        if rows >0 and cols >0:
            row = 0
            col = cols-1

            while row < rows and col > 0:
                if target == arry[row][col]:
                    return True
                elif target < arry[row][col]:
                    col -= 1
                else:
                    row += 1

    return False

if __name__ =='__main__':
    target = 15
    array = [[1,2,3],[4,5,6],[7,8,9],[10,12,13]]
    answer = Solution()
    print(answer.Find(target,array))