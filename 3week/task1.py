"""
https://leetcode.com/problem-list/array/
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1 or len(nums) == 0:
            return len(nums)
        left_ptr, right_ptr = 0, 0
        while right_ptr < len(nums) - 1:
            right_ptr += 1
            if nums[left_ptr] != nums[right_ptr]:
                if (right_ptr - 1) - left_ptr >= 2:
                    del nums[left_ptr + 1: right_ptr - 1]
                    left_ptr += 2
                else:
                    left_ptr = right_ptr
                right_ptr = left_ptr + 1
            elif right_ptr == len(nums) - 1:
                if (right_ptr - 1) - (left_ptr + 1) + 1 >= 1:
                    del nums[left_ptr + 1: right_ptr]
        return len(nums)
