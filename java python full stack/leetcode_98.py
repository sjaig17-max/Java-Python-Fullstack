"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, float("-inf"), float("inf"))


if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    sol = Solution()
    print(sol.isValidBST(root))  # True

    bad_root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(sol.isValidBST(bad_root))  # False
