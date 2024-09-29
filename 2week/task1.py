"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/reverse-words-in-a-string/description/
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        formatted_string = s
        while "  " in formatted_string:
            formatted_string = formatted_string.replace("  ", " ")
        formatted_string.strip()
        result = [word for word in formatted_string.split()]
        result.reverse()

        return ' '.join(result)
