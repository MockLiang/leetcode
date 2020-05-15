'''
@Author: your name
@Date: 2020-04-24 02:46:35
@LastEditTime: 2020-05-15 12:20:27
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/algorithm/twosum1.py
'''


# class Solution:
#     def twoSum(self, nums, target: int):
#         hashmap = {}
#         for i, num in enumerate(nums):
#             hashmap[num] = i
#         for i, num in enumerate(hashmap):
#             j = hashmap.get(target - num)
#             print(i, num)
#             if j and (j != i):
#                 return [i, j]
class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for ind, num in enumerate(nums):
            hashmap[num] = ind
        for i, num in enumerate(nums):
            j = hashmap.get(target - num)
            print(i, num)
            if j is not None and i != j:
                return [i, j]


if __name__ == "__main__":
    nums = [100, 1]
    target = 101
    ret = Solution().twoSum(nums, target)
    for r in ret:
        print(r)
