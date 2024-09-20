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

        maxLength = 0
        letters = set()
        for i in range (0, len(s)):
            letters.clear()
            for j in range(i, len(s)):
                if s[j] not in letters:
                    letters.add(s[j])
                else:
                    maxLength = max(maxLength, len(letters))
                    break
            maxLength = max(maxLength, len(letters))
        return maxLength
