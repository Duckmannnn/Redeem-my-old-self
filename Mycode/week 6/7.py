# https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/
# 1786. Number of Restricted Paths From First to Last Node

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        MOD = 10**9 + 7

        # build graph
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # dijkstra from node n
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        heap = [(0, n)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heapq.heappush(heap, (dist[v], v))

        # dp with memoization
        @lru_cache(maxsize=None)
        def dp(u):
            if u == n:
                return 1
            total = 0
            for v, _ in graph[u]:
                if dist[v] < dist[u]:  # restricted path condition
                    total = (total + dp(v)) % MOD
            return total

        return dp(1)