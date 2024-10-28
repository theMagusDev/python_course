"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/generate-parentheses/
"""

from typing import List


def checkIsValidParenthesisSeq(sequence: List) -> bool:
    checker = list()
    while len(sequence) != 0:
        element = sequence.pop(0)
        if element == "(":
            checker.append("(")
        else:
            if len(checker) == 0 or checker.pop() != "(":
                return False
    if len(checker) != 0:
        return False
    return True


def recursiveParenthesisGenerator(
    left: int, right: int, sequence: str, result: List[str]
):
    if left == 0 and right == 0:
        result.append(sequence)
    if left - 1 >= 0:
        recursiveParenthesisGenerator(left - 1, right, sequence + "(", result)
    if 0 <= right - 1 and right - 1 >= left:
        recursiveParenthesisGenerator(left, right - 1, sequence + ")", result)


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = list()
        recursiveParenthesisGenerator(n - 1, n, "(", result)
        return result
