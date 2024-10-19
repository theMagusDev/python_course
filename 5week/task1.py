"""
https://leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

from typing import List


keyboard = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


def backtracking(result: List[str], digits: str, current_str: str):
    if len(digits) == 0:
        return
    if len(current_str) == len(digits):
        result.append(current_str)
        return
    for i in range(len(keyboard[digits[len(current_str)]])):
        backtracking(
            result, digits, current_str + keyboard[digits[len(current_str)]][i]
        )


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = list()
        backtracking(result, digits, "")
        return result
