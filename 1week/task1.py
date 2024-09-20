"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/count-and-say/description/
"""

class Solution:
    def countAndSay(self, n: int) -> str:
        current_str = "1"
        resulting_str = ""

        left_ptr, right_ptr = 0, 0
        counter = 0
        for i in range(1, n):
            left_ptr, right_ptr = 0, 0
            counter = 0
            resulting_str = ""
            while left_ptr <= len(current_str) - 1:
                while right_ptr <= len(current_str) - 1 and current_str[left_ptr] == current_str[right_ptr]:
                    counter += 1
                    right_ptr += 1
                resulting_str += str(counter) + current_str[left_ptr]
                left_ptr = right_ptr
                counter = 0
            current_str = resulting_str
        return current_str
