'''
@Author: your name
@Date: 2020-05-07 05:11:24
@LastEditTime: 2020-05-15 12:21:00
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/jianzhi/i43_count_digit_one.py
'''
"""
输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。

例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# -*- coding: utf-8 -*-


class Solution:
    # 个人法
    # def countDigitOne(self, n: int) -> int:
    #     res = 0
    #     for i in range(n + 1):
    #         a, b = divmod(i, 10)
    #         count_a, count_b = str(a), str(b)
    #         res = res + count_a.count('1') + count_b.count('1')
    #     return res

    # 
    def countDigitOne(self, n: int) -> int:


print(Solution().countDigitOne(12))
