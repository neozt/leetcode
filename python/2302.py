from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        total = 0
        i = 0
        for j in range(len(nums)):
            total += nums[j]
            while i <= j and total * (j - i + 1) >= k:
                total -= nums[i]
                i += 1

            result += j - i + 1

        return result

print(Solution().countSubarrays([2,1,4,3,5], 10))
print(Solution().countSubarrays([1,1,1], 5))
