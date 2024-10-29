"""
https://leetcode.com/problem-list/array/
https://leetcode.com/problems/next-permutation/
"""

from typing import List


def backtracking(current_index: int, nums: List[int]):
    min_greater = 999
    min_greater_index = -1
    for i in range(len(nums) - 1, current_index + 1, -1):
        if nums[current_index + 1] < nums[i] < min_greater:
            min_greater = nums[i]
            min_greater_index = i
    if min_greater_index == -1 and current_index - 1 >= -1:
        backtracking(current_index - 1, nums)
    else:
        nums[current_index + 1], nums[min_greater_index] = (
            nums[min_greater_index],
            nums[current_index + 1],
        )
        swap_detected = True
        while swap_detected:
            swap_detected = False
            for i in range(current_index + 2, len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    swap_detected = True


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        backtracking(len(nums) - 1, nums)
