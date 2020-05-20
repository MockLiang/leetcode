'''
@Author: your name
@Date: 2020-05-15 12:27:38
@LastEditTime: 2020-05-15 12:42:54
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/sort_algorithm.py
'''
# -*- coding: utf-8 -*-


class Sort(object):

    def merge_sort(self, array):
        if len(array) <= 1:
            return array
        left, right = array[:len(array) // 2], array[len(array) // 2:]

        def merge(left, right):
            res = []
            while left and right:
                if left[0] < right[0]:
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))

            if not left:
                res += right
            else:
                res += left

            return res

        return merge(self.merge_sort(left), self.merge_sort(right))

    def qucik_sort(self, array):
        pass


if __name__ == "__main__":
    array = [3, 1]
    res = Sort().merge_sort(array)
    print(res)
