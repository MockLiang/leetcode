"""
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0，第1项是1）。
n<=39
"""
# -*- coding:utf-8 -*-


# 非递归法
class Solution:
    def Fibonacci(self, n):
        # write code here
        prev, curr = 1, 0
        for _ in range(n):
            prev, curr = curr, prev + curr
        return curr


# 递归法
# class Solution:
#     def Fibonacci(self, n):
#         # write code here
#         if n == 1:
#             return 1
#         if n == 0:
#             return 0
#         return self.Fibonacci(n - 1) + self.Fibonacci(n - 2)


print(Solution().Fibonacci(5))
