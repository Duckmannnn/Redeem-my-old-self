#https://leetcode.com/problems/clone-graph/
#133. Clone Graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        visited = {}  # maps original node → cloned node

        def dfs(n):
            if n in visited: return visited[n]  # already cloned, return to avoid cycle
            clone = Node(n.val)
            visited[n] = clone                  # store BEFORE recursing to handle cycles
            for neighbor in n.neighbors:
                clone.neighbors.append(dfs(neighbor))
            return clone

        return dfs(node)