"""
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，
总共有多少种方法？
比如n=3时，2*3的矩形块有3种覆盖方法
"""
# -*- coding:utf-8 -*-


class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        prev, curr = 0, 1
        for _ in range(number):
            prev, curr = curr, prev + curr
        return curr


print(Solution().rectCover(0))
