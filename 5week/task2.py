"""
https://leetcode.com/problem-list/hash-table/
https://leetcode.com/problems/integer-to-roman/
"""

hmap = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        thousands = num // 1000
        result += hmap[1000] * thousands
        num %= 1000

        # hundreds
        hundreds = num // 100
        if hundreds == 4 or hundreds == 9:
            result += hmap[100] + hmap[(hundreds + 1) * 100]
            num %= hundreds * 100
        hundreds500 = num // 500
        if hundreds500 >= 1:
            result += hmap[500]
            num %= hundreds500 * 500
        hundreds = num // 100
        result += hmap[100] * hundreds
        num %= 100

        # decimals
        decimals = num // 10
        if decimals == 4 or decimals == 9:
            result += hmap[10] + hmap[(decimals + 1) * 10]
            num %= decimals * 10
        decimals50 = num // 50
        if decimals50 >= 1:
            result += hmap[50]
            num %= decimals50 * 50
        decimals = num // 10
        result += hmap[10] * decimals
        num %= 10

        # units
        units = num
        if units == 4 or units == 9:
            result += hmap[1] + hmap[units + 1]
            num %= units
        units5 = num // 5
        if units5 >= 1:
            result += hmap[5]
            num %= units5 * 5
        units = num
        result += hmap[1] * units
        return result
