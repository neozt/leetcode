import heapq
from typing import List


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        m = len(heightMap)
        n = len(heightMap[0])
        heap = []
        visited = [[False] * n for _ in range(m)]

        for i in range(m):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            visited[i][0] = True
            heapq.heappush(heap, (heightMap[i][n - 1], i, n - 1))
            visited[i][-1] = True

        for j in range(n):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            visited[0][j] = True
            heapq.heappush(heap, (heightMap[m - 1][j], m - 1, j))
            visited[-1][j] = True

        water = 0
        while heap:
            h, r, c = heapq.heappop(heap)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    not (0 <= nr < m and 0 <= nc < n)
                    or visited[nr][nc]
                ):
                    continue

                n_height = heightMap[nr][nc]
                if n_height < h:
                    water += h - n_height

                visited[nr][nc] = True
                heapq.heappush(heap, (max(n_height, h), nr, nc))

        return water

print(Solution().trapRainWater([[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]))
print(Solution().trapRainWater([[3,3,3,3,3],[3,2,2,2,3],[3,2,1,2,3],[3,2,2,2,3],[3,3,3,3,3]]))

