'''
@Author: your name
@Date: 2020-05-10 00:47:07
@LastEditTime: 2020-05-10 00:56:35
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/algorithm/p151_reverse_words.py
'''
"""
给定一个字符串，逐个翻转字符串中的每个单词。

"""


class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        words = s.split()
        words = words[::-1]
        return " ".join(words)
