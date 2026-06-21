# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
# 105. Construct Binary Tree from Preorder and Inorder Traversal
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        mid = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

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
print(bfs(sol.buildTree([3,9,20,15,7], [9,3,15,20,7])))  # [3, 9, 20, 15, 7]