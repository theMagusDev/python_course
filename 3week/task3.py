"""
https://leetcode.com/problem-list/array/
https://leetcode.com/problems/search-in-rotated-sorted-array/description/
"""

from math import floor
from typing import List


def bin_search(nums: List[int], target: int, pivot: int) -> int:
    print(f"Got list {nums}")
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = left + floor((right - left) / 2)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return (mid + pivot - 1) % len(nums)
    return -1


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        pivot = -1
        while right - left > 1:
            print(f"left = {left}, right = {right}")
            mid = left + floor((right - left) / 2)
            if nums[mid] > nums[right]:
                left = mid
            elif nums[mid] < nums[right]:
                right = mid
            else:
                break

        if nums[left] < nums[right]:
            print(
                f"left, as {nums[left]}, left = {left} < {nums[right]}, right = {right}"
            )
            pivot = left + 1
        else:
            print("right")
            pivot = right + 1

        pivot %= len(nums)
        if pivot == 1:
            return bin_search(nums, target, pivot)
        else:
            return bin_search(nums[pivot - 1:] + nums[: pivot - 1], target, pivot)
