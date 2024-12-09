"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/compare-version-numbers/description/
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        parsed_version1 = list(map(int, version1.split(".")))
        parsed_version2 = list(map(int, version2.split(".")))
        if len(parsed_version1) < len(parsed_version2):
            for i in range(len(parsed_version2) - len(parsed_version1)):
                parsed_version1.append(0)
        else:
            for i in range(len(parsed_version1) - len(parsed_version2)):
                parsed_version2.append(0)
        for i in range(len(parsed_version1)):
            if parsed_version1[i] < parsed_version2[i]:
                return -1
            elif parsed_version1[i] > parsed_version2[i]:
                return 1
        return 0
