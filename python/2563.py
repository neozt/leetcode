import bisect
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        result = 0
        for i in range(len(nums)):
            left = max(bisect.bisect_left(nums, lower - nums[i]), i + 1)
            right = max(bisect.bisect_right(nums, upper - nums[i]), i + 1)
            result += (right - left)

        return result

print(Solution().countFairPairs([0,1,7,4,4,5], 3, 6))
print(Solution().countFairPairs([1,7,9,2,5], 11, 11))
print(Solution().countFairPairs([0,0,0,0,0,0], 0, 0))

