"""
https://leetcode.com/problem-list/array/
https://leetcode.com/problems/container-with-most-water/description/
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1
        max_volume = 0
        volume = min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr)
        max_volume = max(max_volume, volume)
        while left_ptr < right_ptr:
            if height[left_ptr] < height[right_ptr]:
                left_ptr += 1
            else:
                right_ptr -= 1
            volume = min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr)
            max_volume = max(max_volume, volume)
        return max_volume