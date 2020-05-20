'''
@Author: your name
@Date: 2020-05-06 04:09:18
@LastEditTime: 2020-05-20 23:24:28
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/jianzhi/i24_reverse_list.py
'''
# -*- coding: utf-8 -*-
"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre = head
        if not pre:
            return None
        post = head.next
        pre.next = None

        while post:
            next = post.next
            post.next = pre
            pre = post
            post = next
        return pre
