"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1

        max_length = 0
        letters = set()
        for i in range(0, len(s)):
            letters.clear()
            for j in range(i, len(s)):
                if s[j] not in letters:
                    letters.add(s[j])
                else:
                    max_length = max(max_length, len(letters))
                    break
            max_length = max(max_length, len(letters))
        return max_length
