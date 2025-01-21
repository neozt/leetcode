import math
from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        minimum_sum = math.inf

        for turn_index in range(len(grid[0])):
            first_row_sum -= grid[0][turn_index]
            second_player_point = max(first_row_sum, second_row_sum)
            minimum_sum = min(minimum_sum, second_player_point)
            second_row_sum += grid[1][turn_index]

        return minimum_sum

print(Solution().gridGame([[2,5,4],[1,5,1]]))
print(Solution().gridGame([[3,3,1],[8,5,2]]))
print(Solution().gridGame([[1,3,1,15],[1,3,3,1]]))
