from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.island_size = [1 for _ in range(n)]

    def find(self, n):
        if self.parent[n] == n:
            return n
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)

        if p1 == p2:
            return

        p_smaller = p1
        p_larger = p2
        if self.island_size[p1] > self.island_size[p2]:
            p_smaller = p2
            p_larger = p1

        self.parent[p_smaller] = p_larger
        self.island_size[p_larger] += self.island_size[p_smaller]

class Solution:
    LEFT_AND_UP_DIRECTIONS = [(0, -1), (-1, 0)]
    DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        uf = UnionFind(n * n)

        # Group all land masses
        for row in range(n):
            for col in range(n):
                if grid[row][col] == 0:
                    continue

                for dr, dc in self.LEFT_AND_UP_DIRECTIONS:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= n or nc < 0 or nc >= n:
                        continue

                    n_old = row * n + col
                    n_new = nr * n + nc

                    if grid[nr][nc] == 1:
                        uf.union(n_old, n_new)

        best = max(uf.island_size[r * n + c] for r in range(n) for c in range(n))

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
                    n_new = nr * n + nc
                    n_parent = uf.find(n_new)
                    pr, pc = n_parent // n, n_parent % n
                    if (pr, pc) not in added:
                        size += uf.island_size[pr * n + pc]
                        added.add((pr, pc))

                best = max(best, size)

        return best

print(Solution().largestIsland([[1,0],[0,1]]))
print(Solution().largestIsland([[1,1],[1,0]]))
print(Solution().largestIsland([[1,1],[1,1]]))
print(Solution().largestIsland([[0,1,1,0,0],[0,0,1,1,0],[1,1,0,1,1],[1,1,0,1,0],[0,1,0,0,1]]))
print(Solution().largestIsland([[1]]))
