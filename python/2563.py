import bisect
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        return self.lower_bound(nums, upper + 1) - self.lower_bound(nums, lower)

    def lower_bound(self, nums, value):
        left = 0
        right = len(nums) - 1
        result = 0
        while left < right:
            sum = nums[left] + nums[right]
            if sum < value:
                result += right - left
                left += 1
            else:
                right -= 1

        return result



print(Solution().countFairPairs([0,1,7,4,4,5], 3, 6))
print(Solution().countFairPairs([1,7,9,2,5], 11, 11))
print(Solution().countFairPairs([0,0,0,0,0,0], 0, 0))

