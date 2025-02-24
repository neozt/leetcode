from collections import defaultdict
from typing import List


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)

        shortest_path = None
        def dfs_find_zero(node: int, visited):
            if node in visited:
                return None

            if node == 0:
                return [0]

            visited.add(node)
            for neighbor in adj[node]:
                path = dfs_find_zero(neighbor, visited)
                if path:
                    path = [node] + path
                    return path

            visited.remove(node)
            return None

        path_of_bob = dfs_find_zero(bob, set())

        visited = set()
        levels = [(0, 0)]
        current = 0
        best = -math.inf
        while levels:
            next_level = []
            for node, point in levels:
                visited.add(node)
                if current < len(path_of_bob) and node == path_of_bob[current]:
                    point += amount[node] // 2
                else:
                    point += amount[node]

                is_leaf = True
                for neighbor in adj[node]:
                    if neighbor in visited:
                        continue

                    is_leaf = False
                    next_level.append((neighbor, point))

                if is_leaf:
                    best = max(best, point)

            levels = next_level
            if current < len(path_of_bob):
                amount[path_of_bob[current]] = 0
            current += 1

        return best

