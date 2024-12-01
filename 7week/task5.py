"""
https://leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/contains-duplicate-iii/
"""

from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], indexDiff: int, valueDiff: int
    ) -> bool:
        if valueDiff < 0:
            return False
        bucket = {}
        bucket_size = valueDiff + 1
        for i, num in enumerate(nums):
            bucket_id = num // bucket_size
            if bucket_id in bucket:
                return True
            if (
                bucket_id - 1 in bucket
                and abs(num - bucket[bucket_id - 1]) <= valueDiff
            ):
                return True
            if (
                bucket_id + 1 in bucket
                and abs(num - bucket[bucket_id + 1]) <= valueDiff
            ):
                return True
            bucket[bucket_id] = num
            if i >= indexDiff:
                del bucket[nums[i - indexDiff] // bucket_size]
        return False
