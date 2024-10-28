"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/multiply-strings/
"""

digit_dict = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
}


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        total = 0
        row_shifting = 1
        for i in range(len(num2) - 1, -1, -1):
            current_row = 0
            multiplicator = 1
            i_digit = digit_dict[num2[i]]
            for j in range(len(num1) - 1, -1, -1):
                j_digit = digit_dict[num1[j]]
                current_row += i_digit * j_digit * multiplicator
                multiplicator *= 10
            total += current_row * row_shifting
            row_shifting *= 10
        return str(total)
