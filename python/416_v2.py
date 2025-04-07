from functools import cache
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2

        @cache
        def can_make_sum(index: int, current: int) -> bool:
            if current == target:
                return True

            if index == len(nums):
                return False

            if current > target:
                return False

            return can_make_sum(index + 1, current) or can_make_sum(index + 1, current + nums[index])

        return can_make_sum(0, 0)


print(Solution().canPartition([1, 5, 11, 5]))
print(Solution().canPartition([1, 2, 3, 5]))
