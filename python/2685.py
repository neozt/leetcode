from collections import defaultdict
from typing import List


class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        result = 0

        def dfs(current: int, info: List[int]):
            visited.add(current)
            info[0] += 1
            info[1] += len(adj[current])

            for neighbor in adj[current]:
                if neighbor not in visited:
                    dfs(neighbor, info)

        for i in range(n):
            if i in visited:
                continue

            # node_info[0] = vertices count
            # node_info[1] = edges count
            node_info = [0, 0]
            dfs(i, node_info)

            if node_info[1] == node_info[0] * (node_info[0] - 1):
                result += 1

        return result

print(Solution().countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4]]))
print(Solution().countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4],[3,5]]))
