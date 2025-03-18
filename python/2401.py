from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        longest = 0
        for i in range(len(nums)):
            seen = 0
            for j in range(i, len(nums)):
                current = nums[j]
                if current & seen:
                    break

                seen = current | seen
                longest = max(longest, j - i + 1)

        return longest


print(Solution().longestNiceSubarray([1,3,8,48,10]))
print(Solution().longestNiceSubarray([3,1,5,11,13]))
