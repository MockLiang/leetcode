"""
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
"""
# -*- coding:utf-8 -*-


# 暴力法
# class Solution:
#     def NumberOf1(self, n):
#         # write code here
#         compare = int('0b1111111111111111', 2)
#         num_of_one = 0
#         while n != 0:
#             if n & compare % 2 != 0:
#                 num_of_one = num_of_one + 1
#             n = n >> 1
#         return num_of_one


# 正解法
class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        while n & 0xffffffff != 0:
            count = count + 1
            n = (n - 1) & n
        return count


print(Solution().NumberOf1(-5))
