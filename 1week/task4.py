"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/minimum-window-substring/
"""


def is_dict_in_dict(outer: dict, inner: dict) -> bool:
    for innerKey in inner.keys():
        if not (innerKey in outer.keys() and outer[innerKey] >= inner[innerKey]):
            return False
    return True


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_dict = dict()
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict.update({char: 1})

        s_dict = dict()
        left_ptr, right_ptr = 0, -1
        saved_left_ptr, saved_right_ptr = -10000, 10000
        while right_ptr < len(s):
            if is_dict_in_dict(s_dict, t_dict):
                if right_ptr - left_ptr < saved_right_ptr - saved_left_ptr:
                    saved_left_ptr = left_ptr
                    saved_right_ptr = right_ptr
                s_dict[s[left_ptr]] -= 1
                left_ptr += 1
                continue
            else:
                if right_ptr + 1 >= len(s):
                    break
                right_ptr += 1
                if s[right_ptr] in s_dict:
                    s_dict[s[right_ptr]] += 1
                else:
                    s_dict.update({s[right_ptr]: 1})
        if saved_right_ptr == 10000 and saved_left_ptr == -10000:
            return ""
        return s[saved_left_ptr : saved_right_ptr + 1]
