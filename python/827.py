from collections import defaultdict
from typing import List

class UnionFind:
    def __init__(self, grid):
        self.rows = len(grid)
        self.cols = len(grid)
        self.parent = [[(row, col, grid[row][col]) for col in range(self.cols)] for row in range(self.rows)]

    def find(self, row, col):
        pr, pc, _ = self.parent[row][col]
        ppr, ppc, _ = self.parent[pr][pc]
        while (pr, pc) != (ppr, ppc):
            self.parent[row][col] = self.parent[pr][pc]
            pr, pc, _ = self.parent[row][col]
            ppr, ppc, _ = self.parent[pr][pc]

        return self.parent[pr][pc]

    def union(self, row1, col1, row2, col2):
        p1_row, p1_col, p1_size = self.find(row1, col1)
        p2_row, p2_col, p2_size = self.find(row2, col2)
        new_size = p1_size + p2_size if (p1_row, p1_col) != (p2_row, p2_col) else max(p1_size, p2_size)
        self.parent[p2_row][p2_col] = p1_row, p1_col, -1 # Set parent of node 2 to parent of node 1
        self.parent[p1_row][p1_col] = p1_row, p1_col, new_size # Update size of node 1 parent

    def maximum(self):
        if not self.rows and not self.cols:
            return 0
        return max(self.parent[row][col][2] for col in range(self.cols) for row in range(self.rows))

class Solution:
    LEFT_AND_UP_DIRECTIONS = [(0, -1), (-1, 0)]
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(grid)

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

        best = uf.maximum()

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
                    pr, pc, p_size = uf.find(nr, nc)
                    if (pr, pc) not in added:
                        size += p_size
                        added.add((pr, pc))

                best = max(best, size)

        return best

print(Solution().largestIsland([[1,0],[0,1]]))
print(Solution().largestIsland([[1,1],[1,0]]))
print(Solution().largestIsland([[1,1],[1,1]]))
print(Solution().largestIsland([[0,1,1,0,0],[0,0,1,1,0],[1,1,0,1,1],[1,1,0,1,0],[0,1,0,0,1]]))
print(Solution().largestIsland([[1]]))
