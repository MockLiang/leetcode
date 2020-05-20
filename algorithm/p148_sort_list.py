'''
@Author: your name
@Date: 2020-05-15 12:22:44
@LastEditTime: 2020-05-15 13:00:29
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/algorithm/p148_sort_list.py
'''
"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

"""
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        slow, fast = head, head.next

        while fast and fast.next:
            slow, fast = slow.next, fast.next.next

        mid = slow.next
        slow.next = None

        left, right = self.sortList(head), self.sortList(mid)
        head = ListNode(0)
        res = head
        while left and right:
            if left.val < right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        if left:
            head.next = left
        else:
            head.next = right

        return res.next
