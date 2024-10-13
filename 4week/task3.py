"""
https://leetcode.com/problem-list/array/
https://leetcode.com/problems/permutations-ii/description/
"""

from typing import List


def backtrack(permutations, numbers_to_use, permutation, used_numbers):
    if len(numbers_to_use) == len(permutation):
        tuple_permutation = tuple(permutation)
        if tuple_permutation not in permutations:
            permutations.add(tuple_permutation)
        return
    for i in range(len(numbers_to_use)):
        if not used_numbers[i]:
            used_numbers[i] = True
            permutation.append(numbers_to_use[i])
            backtrack(permutations, numbers_to_use, permutation, used_numbers)
            permutation.pop(-1)
            used_numbers[i] = False


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        answer = set(tuple())
        backtrack(answer, nums, list(), [False for _ in range(len(nums))])
        return [[x for x in tuple_iter] for tuple_iter in answer]
