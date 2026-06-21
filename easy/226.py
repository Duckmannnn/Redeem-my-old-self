# https://leetcode.com/problems/invert-binary-tree/description/
# 226. Invert Binary Tree
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root

# Build [4,2,7,1,3,6,9]
root = TreeNode(4)
root.left = TreeNode(2); root.right = TreeNode(7)
root.left.left = TreeNode(1); root.left.right = TreeNode(3)
root.right.left = TreeNode(6); root.right.right = TreeNode(9)

from collections import deque
def bfs(node):
    q, out = deque([node]), []
    while(q):
        n = q.popleft()
        out.append(n.val)
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)
    return out

sol = Solution()
print(bfs(sol.invertTree(root)))  # [4, 7, 2, 9, 6, 3, 1]