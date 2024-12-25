from typing import List

EMPTY = 0
FRESH = 1
ROTTEN = 2
DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        rot_next = set()
        fresh_oranges = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == ROTTEN:
                    rot_next.add((i, j))
                    grid[i][j] = FRESH

                if grid[i][j] == FRESH:
                    fresh_oranges += 1

        time = -1
        while rot_next:
            temp = set()
            for (i, j) in rot_next:
                if (0 <= i < rows) and (0 <= j < cols) and grid[i][j] == FRESH:
                    fresh_oranges -= 1
                    grid[i][j] = ROTTEN
                    for x, y in DIRECTIONS:
                        next_i, next_j = i + x, j + y
                        temp.add((next_i, next_j))

            rot_next = temp
            if (rot_next):
                time += 1

        return time if fresh_oranges == 0 else -1


print(Solution().orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))
print(Solution().orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))
print(Solution().orangesRotting([[0,2]]))
print(Solution().orangesRotting([[2,2],[1,1],[0,0],[2,0]]))

