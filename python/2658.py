from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        visited = set()
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0

            if (r, c) in visited:
                return 0

            visited.add((r, c))

            return grid[r][c] + sum(dfs(r + dr, c + dc) for dr, dc in directions)

        return max(dfs(r, c) for r in range(rows) for c in range(cols))

print(Solution().findMaxFish([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]]))
print(Solution().findMaxFish([[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]))
