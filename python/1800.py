from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        best = current = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current += nums[i]
            else:
                current = nums[i]

            best = max(best, current)

        return best