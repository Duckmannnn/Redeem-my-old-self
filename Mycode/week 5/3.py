# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
# 102. Binary Tree Level Order Traversal
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def dfs(node, depth):
            if not node: return
            if depth == len(res): res.append([])
            res[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)
        dfs(root, 0)
        return res

# Build [3,9,20,null,null,15,7]
root = TreeNode(3)
root.left = TreeNode(9); root.right = TreeNode(20)
root.right.left = TreeNode(15); root.right.right = TreeNode(7)

sol = Solution()
print(sol.levelOrder(root))  # [[3], [9, 20], [15, 7]]