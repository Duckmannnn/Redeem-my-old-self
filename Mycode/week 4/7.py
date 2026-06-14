#https://leetcode.com/problems/course-schedule/
#207. Course Schedule

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites: graph[b].append(a)  # b → a

        state = [0] * numCourses  # 0: unvisited, 1: visiting, 2: done

        def dfs(n):
            if state[n] == 1: return False  # cycle detected
            if state[n] == 2: return True   # already processed
            state[n] = 1
            for neighbor in graph[n]:
                if not dfs(neighbor): return False
            state[n] = 2
            return True

        for i in range(numCourses):
            if not dfs(i): return False
        return True