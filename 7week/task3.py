"""
https://leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/repeated-dna-sequences/
"""

from typing import List


def findRepeatedDnaSequences(self, s: str) -> List[str]:
    seen = set()
    repeated = set()

    for i in range(len(s) - 9):
        sequence = s[i : i + 10]
        if sequence in seen:
            repeated.add(sequence)
        else:
            seen.add(sequence)
    return list(repeated)
