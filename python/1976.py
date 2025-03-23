import heapq
import math
from collections import defaultdict
from heapq import heappush
from typing import List


class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10 ** 9 + 7

        adj = defaultdict(list)
        for u, v, time in roads:
            adj[u].append((v, time))
            adj[v].append((u, time))

        min_heap: List[tuple[int | float, int]] = [(0, 0)]

        shortest_path = [math.inf] * n
        shortest_path[0] = 0

        path_count = [0] * n
        path_count[0] = 1

        while min_heap:
            distance, node = heapq.heappop(min_heap)

            if distance > shortest_path[node]:
                continue

            for neighbor, neighbor_distance in adj[node]:
                if distance + neighbor_distance < shortest_path[neighbor]:
                    shortest_path[neighbor] = distance + neighbor_distance
                    path_count[neighbor] = path_count[node]
                    heappush(min_heap, (shortest_path[neighbor], neighbor))

                elif distance + neighbor_distance == shortest_path[neighbor]:
                    path_count[neighbor] = (path_count[neighbor] + path_count[node]) % MOD

        return path_count[-1]

print(Solution().countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))
print(Solution().countPaths(2, [[1,0,10]]))


