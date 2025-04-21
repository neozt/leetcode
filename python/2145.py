from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        current = 0
        minimum = 0
        maximum = 0

        for diff in differences:
            current += diff
            minimum = min(minimum, current)
            maximum = max(maximum, current)

        return max(0, (upper - lower) - (maximum - minimum) + 1)

print(Solution().numberOfArrays([1,-3,4], 1, 6))
print(Solution().numberOfArrays([3,-4,5,1,-2], -4, 5))
print(Solution().numberOfArrays([-40], -46, 53))
