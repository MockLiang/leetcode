'''
@Author: your name
@Date: 2020-05-11 01:43:03
@LastEditTime: 2020-05-11 01:46:43
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: /leetcode/algorithm/p695_max_area_of_island.py
'''
# -*- coding: utf-8 -*-
import collections


class Solution:

    def maxAreaOfIsland(self, grid) -> int:
        if not grid or not grid[0]:
            return 0
        row = len(grid)
        col = len(grid[0])
        max_area = 0
        for i, l in enumerate(grid):
            for j, _ in enumerate(l):
                if grid[i][j] != 1:
                    continue
                else:
                    island = {(i, j)}
                    print("hello")
                    queue = collections.deque()
                    queue.append((i, j))
                    # itmp, jtmp = i, j
                    while queue:
                        itmp, jtmp = queue[-1]
                        if itmp > 0:
                            if grid[itmp - 1][jtmp] == 1 and (itmp - 1, jtmp) \
                               not in island:
                                island.add((itmp - 1, jtmp))
                                queue.append((itmp - 1, jtmp))
                        if itmp < row - 1:
                            if grid[itmp + 1][jtmp] == 1 and (itmp + 1, jtmp) \
                               not in island:
                                island.add((itmp + 1, jtmp))
                                queue.append((itmp + 1, jtmp))
                        if jtmp > 0:
                            if grid[itmp][jtmp - 1] == 1 and (itmp, jtmp - 1) \
                               not in island:
                                island.add((itmp, jtmp - 1))
                                queue.append((itmp, jtmp - 1))
                        if jtmp < col - 1:
                            if grid[itmp][jtmp + 1] == 1 and (itmp, jtmp + 1) \
                               not in island:
                                island.add((itmp, jtmp + 1))
                                queue.append((itmp, jtmp + 1))

                        queue.popleft()
                    max_area = max(max_area, len(island))
            return max_area


island = [[0], [1]]

print(Solution().maxAreaOfIsland(island))
