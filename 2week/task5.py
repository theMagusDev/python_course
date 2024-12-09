"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
"""

from typing import List


class Solution:
    def findAnagrams(s: str, p: str) -> List[int]:
        result = list()
        pattern_dict = {chr(char): 0 for char in range(ord("a"), ord("z") + 1)}
        sliding_window_dict = pattern_dict.copy()
        for char in p:
            pattern_dict[char] += 1
        for char in s[: len(p)]:
            sliding_window_dict[char] += 1
        left_ptr, right_ptr = 0, len(p) - 1
        if sliding_window_dict == pattern_dict:
            result.append(0)
        while right_ptr < len(s) - 1:
            sliding_window_dict[s[left_ptr]] -= 1
            left_ptr += 1
            right_ptr += 1
            sliding_window_dict[s[right_ptr]] += 1
            if sliding_window_dict == pattern_dict:
                result.append(left_ptr)
        return result
