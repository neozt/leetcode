import math
from typing import List


class Solution:
    LAND = 0
    WATER = 1

    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        # This question is the equivalent to finding the minimum distance to a water cell for each cell
        # We solve this using DP - The value for a cell is minimum of its neighboring cells values plus 1
        m = len(isWater)
        n = len(isWater[0])
        maximum_val = m * n
        height = [[maximum_val] * n for _ in range(m)]

        # First pass from top left to bottom right. We check the neighboring up and left cells
        for r in range(m):
            for c in range(n):
                if isWater[r][c] == self.WATER:
                    height[r][c] = 0
                else:
                    height_above = height[r-1][c] if r > 0 else maximum_val
                    height_left = height[r][c-1] if c > 0 else maximum_val
                    height[r][c] = min(height_above, height_left) + 1

        # First pass from bottom right to top left. We check the neighboring down and right cells
        for r in reversed(range(m)):
            for c in reversed(range(n)):
                height_below = height[r+1][c] if r < m - 1 else maximum_val
                height_right = height[r][c+1] if c < n - 1 else maximum_val
                height[r][c] = min(height[r][c], min(height_below, height_right) + 1)

        return height

print(Solution().highestPeak([[0,1],[0,0]]))
print(Solution().highestPeak([[0,0,1],[1,0,0],[0,0,0]]))
