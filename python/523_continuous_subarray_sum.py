from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total = (total + nums[j]) % k
                if j - i > 0 and total == 0:
                    return True

        return False


print(Solution().checkSubarraySum([23, 2, 4, 6, 7], 6))
print(Solution().checkSubarraySum([23,2,6,4,7], 6))
print(Solution().checkSubarraySum([23,2,6,4,7], 13))
print(Solution().checkSubarraySum([23,2,4,6,6], 7))
print(Solution().checkSubarraySum([5,0,0,0], 3))
