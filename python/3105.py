from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        best = increasing = decreasing = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                increasing += 1
            else:
                increasing = 1

            if nums[i] < nums[i-1]:
                decreasing += 1
            else:
                decreasing = 1

            best = max(best, increasing, decreasing)

        return best