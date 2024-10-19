"""
https://leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/sender-with-largest-word-count/
"""

from typing import List


class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        words_used = {sender: 0 for sender in senders}
        largest_senders = list()
        largest_sender_number = 0
        for i in range(len(messages)):
            words_used[senders[i]] += len(messages[i].split())
            if words_used[senders[i]] > largest_sender_number:
                largest_sender_number = words_used[senders[i]]

        for i in range(len(senders)):
            if words_used[senders[i]] == largest_sender_number:
                largest_senders.append(senders[i])
        if len(largest_senders) > 1:
            largest_senders.sort(reverse=True)
        return largest_senders[0]
