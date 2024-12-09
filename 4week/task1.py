"""
https://leetcode.com/problem-list/array/
https://leetcode.com/problems/valid-sudoku/description
"""

from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        raw_dicts = [
            {chr(x): 0 for x in range(ord("1"), ord("9") + 1)} for i in range(9)
        ]
        column_dicts = [
            {chr(x): 0 for x in range(ord("1"), ord("9") + 1)} for i in range(9)
        ]
        square_dicts = [
            {chr(x): 0 for x in range(ord("1"), ord("9") + 1)} for i in range(9)
        ]
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] != ".":
                    # raw dict
                    raw_dicts[i][board[i][j]] += 1
                    if raw_dicts[i][board[i][j]] == 2:
                        return False
                    # column dict
                    column_dicts[j][board[i][j]] += 1
                    if column_dicts[j][board[i][j]] == 2:
                        return False
                    # square dict
                    square_dicts[(i // 3) * 3 + (j // 3)][board[i][j]] += 1
                    if square_dicts[(i // 3) * 3 + (j // 3)][board[i][j]] == 2:
                        return False
        return True
