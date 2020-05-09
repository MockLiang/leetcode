'''
@Author: your name
@Date: 2020-05-06 04:26:37
@LastEditTime: 2020-05-07 04:53:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/jianzhi/i32_level_order.py
'''
# -*- coding: utf-8 -*-
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res, q = [], deque()
        q.append(root)
        while q:
            curr_node = q.popleft()
            res.append(curr_node.val)
            if curr_node.left:
                q.append(curr_node.left)
            if curr_node.right:
                q.append(curr_node.right)
        return res

