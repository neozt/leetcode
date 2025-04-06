from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        # dp[i] is the length of longest chain starting from i
        dp = [1] * len(nums)
        prev = [-1] * len(nums)
        best =  0

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j

            if dp[i] > dp[best]:
                best = i

        # Reconstruct the longest chain
        current = best
        longest = []
        while current != -1:
            longest.append(nums[current])
            current = prev[current]

        return longest

print(Solution().largestDivisibleSubset([1,2,3]))
print(Solution().largestDivisibleSubset([1,2,4,8]))
print(Solution().largestDivisibleSubset([1]))
