from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        dp = [[nums[i]] for i in range(len(nums))]

        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0 and len(dp[j]) + 1 > len(dp[i]):
                    dp[i] = [nums[i]] + dp[j]

        longest = []
        for l in dp:
            if len(l) > len(longest):
                longest = l

        return longest

print(Solution().largestDivisibleSubset([1,2,3]))
print(Solution().largestDivisibleSubset([1,2,4,8]))
