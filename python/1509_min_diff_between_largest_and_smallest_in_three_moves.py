from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return 0

        nums.sort()

        best = float('inf')
        for i in range(4):
            temp = nums[-4+i] - nums[i]
            best = min(best, temp)
        return best


# print(Solution().minDifference([5,3,2,4]))
# print(Solution().minDifference([1,5,0,10,14]))
# print(Solution().minDifference([3, 10, 20]))
print(Solution().minDifference([6,6,0,1,1,4,6]))
# print(Solution().minDifference([9, 31, 48, 48, 81, 92]))


# [0,1,1,4,6,6,6]


