"""
https://leetcode.com/problem-list/binary-tree/
https://leetcode.com/problems/unique-binary-search-trees-ii/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> list[Optional[TreeNode]]:
        if n == 0:
            return []

        def generate(start, end):
            if start > end:
                return [None]

            result = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        result.append(root)
            return result

        return generate(1, n)
