# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# 104. Maximum Depth of Binary Tree
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Build [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9); root.right = TreeNode(20)
root.right.left = TreeNode(15); root.right.right = TreeNode(7)

sol = Solution()
print(sol.maxDepth(root))  # 3