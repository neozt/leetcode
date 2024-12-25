from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for i in range(m)]

        count = 0
        for i in range(m):
            for j in range(n):
                if (self.markNewIsland(grid, visited, i, j)):
                    count += 1

        return count

    def markNewIsland(self, grid: List[List[str]], visited: List[List[bool]], m: int, n: int) -> bool:
        if not 0 <= m < len(grid) or not 0 <= n < len(grid[0]):
            # Out of bounds
            return False

        if grid[m][n] != "1":
            # Not island
            return False

        if (visited[m][n]):
            # Already visited this island
            return False

        # Visit the whole island and return True to indicate a new island is found
        visited[m][n] = True
        self.markNewIsland(grid, visited, m + 1, n)
        self.markNewIsland(grid, visited, m - 1, n)
        self.markNewIsland(grid, visited, m, n + 1)
        self.markNewIsland(grid, visited, m, n - 1)
        return True


print(Solution().numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))

print(Solution().numIslands([
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
]
))