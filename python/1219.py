from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        best = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i, j, visited, current: int):
            if not 0 <= i < m or not 0 <= j < n:
                return

            if visited[i][j]:
                return

            if grid[i][j] == 0:
                return

            current = current + grid[i][j]
            nonlocal best
            best = max(best, current)
            visited[i][j] = True

            for delta_i, delta_j in ((0, 1), (0, -1), (1, 0), (-1, 0)):
                dfs(i + delta_i, j + delta_j, visited, current)

            visited[i][j] = False

        for i in range(m):
            for j in range(n):
                visited = [[False] * n for _ in range(m)]
                dfs(i, j, visited, 0)

        return best


# print(Solution().getMaximumGold(
#     [
#         [0 , 0 , 0 , 0 , 0 , 0 , 32, 0 , 0 , 20],
#         [0 , 0 , 2 , 0 , 0 , 0 , 0 , 40, 0 , 32],
#         [13, 20, 36, 0 , 0 , 0 , 20, 0 , 0 , 0 ],
#         [0 , 31, 27, 0 , 19, 0 , 0 , 25, 18, 0 ],
#         [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ],
#         [0 , 0 , 0 , 0 , 0 , 0 , 0 , 18, 0 , 6 ],
#         [0 , 0 , 0 , 25, 0 , 0 , 0 , 0 , 0 , 0 ],
#         [0 , 0 , 0 , 21, 0 , 30, 0 , 0 , 0 , 0 ],
#         [19, 10, 0 , 0 , 34, 0 , 2 , 0 , 0 , 27],
#         [0 , 0 , 0 , 0 , 0 , 34, 0 , 0 , 0 , 0 ]
#
#     ]))
print(Solution().getMaximumGold([[1, 0, 7], [2, 0, 6], [3, 4, 5], [0, 3, 0], [9, 0, 20]]))

print(Solution().getMaximumGold([[0, 6, 0],
                                 [5, 8, 7],
                                 [0, 9, 0]]))
# print(Solution().getMaximumGold([[1, 0, 7],
#                                  [2, 0, 6],
#                                  [3, 4, 5],
#                                  [0, 3, 0],
#                                  [9, 0, 20]]))

# print(Solution().getMaximumGold([[0, 0, 19, 5, 8], [11, 20, 14, 1, 0], [0, 0, 1, 1, 1], [0, 2, 0, 2, 0]]))

print(sum([2, 13, 20, 36, 31, 27]))