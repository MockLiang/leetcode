'''
@Date: 2020-05-25 01:35:04
@LastEditors: OBKoro1
@LastEditTime: 2020-05-25 01:56:44
'''
"""
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

注意:

每个数组中的元素不会超过 100
数组的大小不会超过 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# -*- coding: utf-8 -*-


class Solution:
    def canPartition(self, nums: List[int]) -> bool: