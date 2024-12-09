"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/group-anagrams/
"""

from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = strs.copy()
        for i in range(len(sorted_strs)):
            sorted_strs[i] = "".join(sorted([c for c in strs[i]]))
        groups = dict()
        for i in range(len(sorted_strs)):
            if sorted_strs[i] not in groups:
                groups.update({sorted_strs[i]: [strs[i]]})
            else:
                groups[sorted_strs[i]].append(strs[i])
        return [elements for elements in groups.values()]
