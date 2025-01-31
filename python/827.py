from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, rows, cols):
        self.parent = [[(row, col) for col in range(cols)] for row in range(rows)]

    def find(self, row, col):
        pr, pc = self.parent[row][col]
        while self.parent[row][col] != self.parent[pr][pc]:
            self.parent[row][col] = self.parent[pr][pc]
            pr, pc = self.parent[row][col]
        return self.parent[row][col]

    def union(self, row1, col1, row2, col2):
        p1_row, p1_col = self.find(row1, col1)
        p2_row, p2_col = self.find(row2, col2)
        self.parent[p2_row][p2_col] = p1_row, p1_col


class Solution:
    LEFT_AND_UP_DIRECTIONS = [(0, -1), (-1, 0)]
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n, n)
        # Group all land masses
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue

                for dr, dc in self.LEFT_AND_UP_DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= n or nc < 0 or nc >= n:
                        continue

                    if grid[nr][nc] == 1:
                        uf.union(nr, nc, row, col)

        # Calculate size of each land masses
        group_size = defaultdict(int)
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue

                parent = uf.find(row, col)
                group_size[parent] += 1

        best = max(group_size.values()) if len(group_size) > 0 else 0

        # Turn each 0 to 1, combine with neighboring land masses, and find new area
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    continue

                added = set()
                size = 1
                for dr, dc in self.DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= n or nc < 0 or nc >= n or grid[nr][nc] == 0:
                        continue
                    pr, pc = uf.find(nr, nc)
                    if (pr, pc) not in added:
                        size += group_size[(pr, pc)]
                        added.add((pr, pc))

                best = max(best, size)

        return best


print(Solution().largestIsland([[1,0],[0,1]]))
print(Solution().largestIsland([[1,1],[1,0]]))
print(Solution().largestIsland([[1,1],[1,1]]))
print(Solution().largestIsland([[0,1,1,0,0],[0,0,1,1,0],[1,1,0,1,1],[1,1,0,1,0],[0,1,0,0,1]]))
