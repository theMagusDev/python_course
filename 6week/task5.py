"""
https://leetcode.com/problem-list/string/
https://leetcode.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = s[0]
        longest_palindrome_length = 1
        for mid in range(len(s)):
            left = mid
            right = mid
            while (
                left - 1 >= 0
                and right + 1 <= len(s) - 1
                and s[left - 1] == s[right + 1]
            ):
                left -= 1
                right += 1
            current_length = right - left + 1
            if current_length > longest_palindrome_length:
                longest_palindrome_length = current_length
                print(left, mid, right)
                longest_palindrome = s[left : right + 1]
        for mid in range(len(s) - 1):
            left = mid
            right = mid + 1
            if s[left] != s[right]:
                continue
            while (
                left - 1 >= 0
                and right + 1 <= len(s) - 1
                and s[left - 1] == s[right + 1]
            ):
                left -= 1
                right += 1
            current_length = right - left + 1
            if current_length > longest_palindrome_length:
                longest_palindrome_length = current_length
                print(left, mid, right)
                longest_palindrome = s[left : right + 1]
        return longest_palindrome
