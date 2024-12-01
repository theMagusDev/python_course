"""
https://leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/arithmetic-slices
"""

from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count = 0
        current = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                current += 1
                count += current
            else:
                current = 0
        return count
