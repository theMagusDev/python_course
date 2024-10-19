"""
https://leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/top-k-frequent-elements/
"""

from typing import List
from queue import PriorityQueue


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        number_set = set(nums)
        priority_queue = PriorityQueue()
        numbers_frequency = dict()
        for number in nums:
            if number not in numbers_frequency.keys():
                numbers_frequency.update({number: 1})
            else:
                numbers_frequency[number] += 1
        for number, frequency in numbers_frequency.items():
            priority_queue.put((-frequency, number))
        answer = list()
        for i in range(k):
            answer.append(priority_queue.get()[1])
        return answer
