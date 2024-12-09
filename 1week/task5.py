"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/set-matrix-zeroes/description/
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zero_rows = set()
        zero_columns = set()
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_columns.add(j)
        for zero_row in zero_rows:
            for j in range(n):
                matrix[zero_row][j] = 0
        for zero_column in zero_columns:
            for i in range(m):
                matrix[i][zero_column] = 0
