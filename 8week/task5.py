"""
https://leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/longest-turbulent-subarray/
"""

from typing import List


class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1:
            return 1
        max_length = 1
        inc = dec = 1
        for i in range(1, n):
            if arr[i] > arr[i - 1]:
                inc = dec + 1
                dec = 1
            elif arr[i] < arr[i - 1]:
                dec = inc + 1
                inc = 1
            else:
                inc = dec = 1
            max_length = max(max_length, inc, dec)
        return max_length
