# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
# 297. Serialize and Deserialize Binary Tree
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ---- SUBMIT CHỈ PHẦN NÀY ----
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ','.join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = iter(data.split(','))
        def dfs():
            val = next(vals)
            if val == 'N': return None
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
# ------------------------------

root = TreeNode(3)
root.left = TreeNode(9); root.right = TreeNode(20)
root.right.left = TreeNode(15); root.right.right = TreeNode(7)

codec = Codec()
data = codec.serialize(root)
print(data)                          # 3,9,N,N,20,15,N,N,7,N,N
print(codec.serialize(codec.deserialize(data)))  # same → correct