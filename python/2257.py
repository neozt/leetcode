from typing import List


class Solution:
    WALL = 'W'
    GUARD = 'G'
    MARKED = '1'
    UNMARKED = '0'

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[self.UNMARKED] * n for _ in range(m)]

        for wall in walls:
            r, c = wall
            grid[r][c] = self.WALL

        for guard in guards:
            r, c = guard
            grid[r][c] = self.GUARD

        for guard in guards:
            r, c = guard
            # Mark downwards
            for i in range(r + 1, m):
                if grid[i][c] == self.WALL or grid[i][c] == self.GUARD:
                    break
                grid[i][c] = self.MARKED

            # Mark upwards
            for i in range(r - 1, -1, -1):
                if grid[i][c] == self.WALL or grid[i][c] == self.GUARD:
                    break
                grid[i][c] = self.MARKED

            # Mark right
            for i in range(c + 1, n):
                if grid[r][i] == self.WALL or grid[r][i] == self.GUARD:
                    break
                grid[r][i] = self.MARKED

            # Mark left
            for i in range(c - 1, -1, -1):
                if grid[r][i] == self.WALL or grid[r][i] == self.GUARD:
                    break
                grid[r][i] = self.MARKED

        return sum(1 if grid[i][j] == self.UNMARKED else 0 for i in range(m) for j in range(n))


print(Solution().countUnguarded(4, 6, [[0, 0], [1, 1], [2, 3]], [[0, 1], [2, 2], [1, 4]]))
print(Solution().countUnguarded(3, 3, [[1,1]], [[0,1],[1,0],[2,1],[1,2]]))
