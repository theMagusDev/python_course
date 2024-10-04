"""
https://leetcode.com/problem-list/array/
https://leetcode.com/problems/jump-game-ii/description/
"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        power_list = [nums[i] + i for i in range(len(nums))]
        current_positon = 0
        counter = 0
        while current_positon != len(nums) - 1:
            print(f"{current_positon}")
            best_jump_index = -1
            best_jump_power = -1
            if power_list[current_positon] <= len(nums) - 1:
                upper_bound_including = power_list[current_positon]
            else:
                upper_bound_including = len(nums) - 1
            print(f"Upper bound is {upper_bound_including}")
            for i in range(current_positon + 1, upper_bound_including + 1):
                print(f"Considering jumping from {current_positon} to {i} with power {power_list[i]}")
                if i == len(nums) - 1:
                    best_jump_index = i
                    break
                if best_jump_power <= power_list[i]:
                    best_jump_power = power_list[i]
                    best_jump_index = i
            current_positon = best_jump_index
            counter += 1
        return counter