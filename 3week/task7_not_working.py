"""
https://leetcode.com/problem-list/array/
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/
"""
from typing import List
from math import floor, ceil


def bin_search(nums: List[int], target: int, floor_enabled: bool, stop_when_found: bool) -> int:
    left, right = 0, len(nums) - 1
    print(f"With {nums} search {target}")
    hold = -1
    while left <= right:
        print(f"With {nums} search {target} progress: l = {left}, r = {right}")
        if floor_enabled == True:
            mid = left + floor((right - left) / 2)
        else:
            mid = left + ceil((right - left) / 2)
        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            if stop_when_found == True:
                return mid
            else:
                if hold == mid:
                    return mid
                hold = mid
    return hold

class Solution:
    def searchRange(nums: List[int], target: int) -> List[int]:
        mid = bin_search(nums, target, True, True)
        if mid == -1:
            return [-1, -1]
        start = end = mid
        print(f"Found {mid}")
        if mid-1 >= 0 and nums[mid-1] == nums[mid]:
            start = bin_search(nums[:mid], target, True, False)
        if mid+1 <= len(nums) - 1 and nums[mid+1] == nums[mid]:
            end = mid + bin_search(nums[mid+1:], target, False, False) + 1
        return [start, end]

sol = Solution
print(sol.searchRange(nums=[1,1,1,1,1,1,2,3,4,4,5,5,5,6,7,8,8,8,8], target=8))