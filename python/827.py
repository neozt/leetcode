from typing import List

class CoordinatesMapper:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def to_index(self, row, col):
        return row * self.cols + col

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.island_size = [1 for _ in range(n)]

    def find_root(self, n):
        if self.parent[n] == n:
            return n
        self.parent[n] = self.find_root(self.parent[n])
        return self.parent[n]

    def find_size(self, n):
        parent = self.find_root(n)
        return self.island_size[parent]

    def union(self, n1, n2):
        p1 = self.find_root(n1)
        p2 = self.find_root(n2)

        if p1 == p2:
            return

        is_p2_smaller = self.island_size[p1] > self.island_size[p2]
        p_smaller = p2 if is_p2_smaller else p1
        p_larger = p1 if is_p2_smaller else p2

        self.parent[p_smaller] = p_larger
        self.island_size[p_larger] += self.island_size[p_smaller]

class Solution:
    LEFT_AND_UP_DIRECTIONS = [(0, -1), (-1, 0)]
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n * n)
        coordinates_mapper = CoordinatesMapper(n, n)

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
                        uf.union(coordinates_mapper.to_index(row, col), coordinates_mapper.to_index(nr, nc))

        best = max(uf.island_size[coordinates_mapper.to_index(r, c)] for r in range(n) for c in range(n))

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
                    n_parent = uf.find_root(coordinates_mapper.to_index(nr, nc))
                    if n_parent not in added:
                        size += uf.find_size(n_parent)
                        added.add(n_parent)

                best = max(best, size)

        return best

print(Solution().largestIsland([[1,0],[0,1]]))
print(Solution().largestIsland([[1,1],[1,0]]))
print(Solution().largestIsland([[1,1],[1,1]]))
print(Solution().largestIsland([[0,1,1,0,0],[0,0,1,1,0],[1,1,0,1,1],[1,1,0,1,0],[0,1,0,0,1]]))
print(Solution().largestIsland([[1]]))
