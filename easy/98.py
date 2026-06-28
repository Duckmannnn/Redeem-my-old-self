# https://leetcode.com/problems/validate-binary-search-tree/
# 98. Validate Binary Search Tree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidNode(self, node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
        if node is None:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return self.isValidNode(node.left, min_val, node.val) \
           and self.isValidNode(node.right, node.val, max_val)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.isValidNode(root, float('-inf'), float('inf'))