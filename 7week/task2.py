"""
https://leetcode.com/problem-list/sliding-window/
https://leetcode.com/problems/find-k-closest-elements/
"""


def find_closest_elements(arr, k, x):
    left, right = 0, len(arr) - k
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left : left + k]
