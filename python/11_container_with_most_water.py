from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        best_area = 0

        l, r = 0, len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            best_area = max(area, best_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return best_area


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(Solution().maxArea([1, 1]))
print(Solution().maxArea([]))
