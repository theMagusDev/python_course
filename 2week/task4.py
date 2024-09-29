"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/permutation-in-string/description/
"""


class Solution:
    def checkInclusion(s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        string1_letters = {chr(char): 0 for char in range(ord('a'), ord('z')+1)}
        for char in s1:
            string1_letters[char] += 1
        sliding_window = {chr(char): 0 for char in range(ord('a'), ord('z')+1)}
        for i in range(len(s1)):
            sliding_window[s2[i]] += 1
        left_ptr = 0
        right_ptr = len(s1) - 1
        if string1_letters == sliding_window:
            return True
        while right_ptr + 1 < len(s2):
            sliding_window[s2[left_ptr]] -= 1
            left_ptr += 1
            right_ptr += 1
            sliding_window[s2[right_ptr]] += 1
            if string1_letters == sliding_window:
                return True
        return False
