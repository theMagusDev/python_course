"""
https://leetcode.com/problem-list/array/
https://leetcode.com/problems/jump-game/description/
"""
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        power_list = [nums[i] + i for i in range(len(nums))]
        power_list[-1] = 0
        current_positon = 0
        prev_position = -1
        while current_positon != prev_position:
            prev_position = current_positon
            best_jump_index = -1
            best_jump_power = -1
            if power_list[current_positon] <= len(nums) - 1:
                upper_bound_including = power_list[current_positon]
            else:
                upper_bound_including = len(nums) - 1
            for i in range(current_positon + 1, upper_bound_including + 1):
                if i == len(nums) - 1:
                    return True
                if best_jump_power <= power_list[i]:
                    best_jump_power = power_list[i]
                    best_jump_index = i
            current_positon = best_jump_index
            if nums[current_positon] == 0:
                return False
        return False
