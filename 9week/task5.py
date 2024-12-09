"""
https://leetcode.com/problem-list/binary-tree/
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder:
            return None

        root_val = postorder[-1]
        root = TreeNode(root_val)
        root_index = inorder.index(root_val)

        root.left = self.buildTree(inorder[:root_index], postorder[:root_index])
        root.right = self.buildTree(inorder[root_index + 1 :], postorder[root_index:-1])

        return root
