"""
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法
（先后次序不同算不同的结果）。
"""


# -*- coding:utf-8 -*-


# 递归法
# class Solution:
#     def jumpFloor(self, number):
#         # write code here
#         if number == 1:
#             return 1
#         if number == 0:
#             return 0
#         return self.jumpFloor(number - 1) + self.jumpFloor(number - 2)


# 非递归法
class Solution:
    def jumpFloor(self, number):
        # write code here
        prev, curr = 0, 1
        for _ in range(number):
            prev, curr = curr, prev + curr

        return curr
