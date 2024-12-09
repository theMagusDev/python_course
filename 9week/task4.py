"""
https://leetcode.com/problem-list/binary-tree/
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        root_index = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : root_index + 1], inorder[:root_index])
        root.right = self.buildTree(
            preorder[root_index + 1 :], inorder[root_index + 1 :]
        )

        return root
