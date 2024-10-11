"""
https://leetcode.com/problem-list/array/
https://leetcode.com/problems/permutations/description/
"""
from typing import List


def backtrack(permutations, numbers_to_use, permutation, used_numbers):
    if len(numbers_to_use) == len(permutation):
        permutations.append(permutation.copy())
        return
    for i in range(len(numbers_to_use)):
        if not used_numbers[numbers_to_use[i]]:
            used_numbers[numbers_to_use[i]] = True
            permutation.append(numbers_to_use[i])
            backtrack(permutations, numbers_to_use, permutation, used_numbers)
            permutation.pop(-1)
            used_numbers[numbers_to_use[i]] = False


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = list(list())
        backtrack(answer, nums, list(), {x: False for x in nums})
        return answer
