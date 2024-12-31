from collections import defaultdict
from typing import List


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)

        ancestors = [set() for _ in range(n)]

        def dfs(current, parent):
            if parent is not None:
                ancestors[current].add(parent)
                for node in ancestors[parent]:
                    ancestors[current].add(node)

            for neighbor in adj[current]:
                dfs(neighbor, current)

        for i in range(n):
            if not ancestors[i]:
                dfs(i, None)


        result = []
        for i in range(n):
            result.append(sorted(ancestors[i]))

        return result


print(Solution().getAncestors(8, [[0, 3], [0, 4], [1, 3], [2, 4], [2, 7], [3, 5], [3, 6], [3, 7], [4, 6]]))
