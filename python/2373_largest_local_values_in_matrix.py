from typing import List


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        result = [[0] * (cols - 2) for _ in range(rows - 2)]

        for i in range(1, rows - 1):
            for j in range(1, cols - 1):
                localMax = max(grid[x][y] for x in range(i - 1, i + 2) for y in range(j - 1, j + 2))
                result[i-1][j-1] = localMax

        return result


print(Solution().largestLocal([[9, 9, 8, 1], [5, 6, 2, 6], [8, 2, 6, 4], [6, 2, 2, 2]]))
print(Solution().largestLocal([[1,1,1,1,1],[1,1,1,1,1],[1,1,2,1,1],[1,1,1,1,1],[1,1,1,1,1]]))