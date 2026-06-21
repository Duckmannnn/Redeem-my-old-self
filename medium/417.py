# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
# 417. Pacific Atlantic Water Flow
from typing import List

# ---- SUBMIT CHỈ PHẦN NÀY ----
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, visited):
            visited.add((r, c))
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and heights[nr][nc] >= heights[r][c]:
                    dfs(nr, nc, visited)

        pac, atl = set(), set()
        for r in range(rows):
            dfs(r, 0, pac)
            dfs(r, cols-1, atl)
        for c in range(cols):
            dfs(0, c, pac)
            dfs(rows-1, c, atl)

        return [[r,c] for r in range(rows) for c in range(cols) if (r,c) in pac and (r,c) in atl]
# ------------------------------

sol = Solution()
print(sol.pacificAtlantic([
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]))  # [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]