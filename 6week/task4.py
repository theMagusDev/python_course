"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/word-search/
"""

from typing import List


def backtracking(
    board: List[List[str]],
    word: str,
    temp_word: str,
    i,
    j,
    visited_cells: set,
    answer: List,
):
    if len(temp_word) == len(word):
        if temp_word == word:
            answer.append(True)
        return

    up = board[i - 1][j]
    down = board[i + 1][j]
    left = board[i][j - 1]
    right = board[i][j + 1]
    new_visited_cells = visited_cells.copy()
    new_visited_cells.add((i, j))
    if up == word[len(temp_word)] and up != "#" and (i - 1, j) not in visited_cells:
        backtracking(board, word, temp_word + up, i - 1, j, new_visited_cells, answer)

    if down == word[len(temp_word)] and down != "#" and (i + 1, j) not in visited_cells:
        backtracking(board, word, temp_word + down, i + 1, j, new_visited_cells, answer)

    if left == word[len(temp_word)] and left != "#" and (i, j - 1) not in visited_cells:
        backtracking(board, word, temp_word + left, i, j - 1, new_visited_cells, answer)

    if (
        right == word[len(temp_word)]
        and right != "#"
        and (i, j + 1) not in visited_cells
    ):
        backtracking(
            board, word, temp_word + right, i, j + 1, new_visited_cells, answer
        )


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 1 and len(board[0]) == 1 and board[0][0] == word:
            return True
        if len(board) == 0:
            return False

        extended_board = list()
        extended_board.append(["#" for _ in range(len(board[0]) + 2)])
        for i in range(len(board)):
            extended_board.append(["#"] + [cell for cell in board[i]] + ["#"])
        extended_board.append(["#" for _ in range(len(board[0]) + 2)])
        answer = list()
        for i in range(1, len(extended_board) - 1):
            for j in range(1, len(extended_board[0]) - 1):
                backtracking(
                    extended_board, word, extended_board[i][j], i, j, set(), answer
                )
        return len(answer) > 0
