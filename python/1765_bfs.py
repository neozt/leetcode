from collections import deque
from typing import List


class Solution:
    LAND = 0
    WATER = 1
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # Solve using multi-source BFS
        m = len(isWater)
        n = len(isWater[0])
        height = [[-1] * n for _ in range(m)]
        q = deque()

        for r in range(m):
            for c in range(n):
                if isWater[r][c] == self.WATER:
                    height[r][c] = 0
                    q.append((r,c,0))

        while q:
            r, c, h = q.popleft()
            for dr, dc in self.DIRECTIONS:
                nr, nc = r + dr, c + dc
                nh = h + 1
                if 0 <= nr < m and 0 <= nc < n and height[nr][nc] == -1:
                    height[nr][nc] = nh
                    q.append((nr,nc,nh))

        return height

print(Solution().highestPeak([[0,1],[0,0]]))
print(Solution().highestPeak([[0,0,1],[1,0,0],[0,0,0]]))