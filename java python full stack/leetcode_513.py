"""
513. Find Bottom Left Tree Value
https://leetcode.com/problems/find-bottom-left-tree-value/
"""
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        result = root.val
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                node = queue.popleft()
                if i == 0:
                    result = node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result


if __name__ == "__main__":
    root = TreeNode(2, TreeNode(1), TreeNode(3))
    sol = Solution()
    print(sol.findBottomLeftValue(root))  # 1
