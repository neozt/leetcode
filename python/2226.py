import math
from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        left = 0
        right = max(candies)

        while left < right:
            mid = math.ceil((left + right) / 2)

            if can_distribute_candies(candies, k, mid):
                left = mid
            else:
                right = mid - 1

        return left


def can_distribute_candies(candies: List[int], k: int, c: int) -> int:
    subpiles = 0
    for pile in candies:
        subpiles += pile // c
        if subpiles >= k:
            return True

    return False


print(Solution().maximumCandies([5,8,6], 3))
print(Solution().maximumCandies([2,5], 11))
print(Solution().maximumCandies([4,7,5], 4))
