"""
https://leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/top-k-frequent-words/
"""

from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words_frequency = dict()
        for i in range(len(words)):
            if words[i] not in words_frequency:
                words_frequency.update({words[i]: 1})
            else:
                words_frequency[words[i]] += 1
        answer = sorted(
            [(frequency, word) for word, frequency in words_frequency.items()],
            key=lambda x: (-x[0], x[1]),
        )
        k_first = list()
        for i in range(k):
            k_first.append(answer[i][1])
        return k_first
