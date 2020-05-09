'''
@Author: your name
@Date: 2020-05-09 23:24:54
@LastEditTime: 2020-05-10 00:46:49
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/algorithm/p15_three_sum.py
'''
"""
给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
# -*- coding: utf-8 -*-


class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return None

        nums.sort()
        res = []
        for i, _ in enumerate(nums):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    right -= 1

        return res


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
