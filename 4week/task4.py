"""
https://leetcode.com/problem-list/array/
https://leetcode.com/problems/minimum-path-sum/
"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp_grid = [[0 for _ in range(len(grid[0]))] for __ in range(len(grid))]
        dp_grid[0][0] = grid[0][0]
        for i in range(1, len(dp_grid)):
            dp_grid[i][0] = dp_grid[i - 1][0] + grid[i][0]
        for j in range(1, len(dp_grid[0])):
            dp_grid[0][j] = dp_grid[0][j - 1] + grid[0][j]
        for i in range(1, len(dp_grid)):
            for j in range(1, len(dp_grid[0])):
                dp_grid[i][j] = grid[i][j] + min(dp_grid[i - 1][j], dp_grid[i][j - 1])
        return dp_grid[len(dp_grid) - 1][len(dp_grid[0]) - 1]
