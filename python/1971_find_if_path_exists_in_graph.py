from collections import defaultdict
from typing import List


class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for (v1, v2) in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)

        return self.dfs(graph, source, destination, set())

    def dfs(self, graph, source, destination, visited):
        if source in visited:
            return False

        if source == destination:
            return True

        visited.add(source)

        return any(self.dfs(graph, neighbor, destination, visited) for neighbor in graph[source])


print(Solution().validPath(3, [[0, 1], [1, 2], [2, 0]], 0, 2))
print(Solution().validPath(6, [[0,1],[0,2],[3,5],[5,4],[4,3]], 0, 5))
print(Solution().validPath(10, [[0,7],[0,8],[6,1],[2,0],[0,4],[5,8],[4,7],[1,3],[3,5],[6,5]], 7, 5))