from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # Sliding window
        used = 0 # keep track of which bit already used in current window
        longest = 0
        start = 0

        for end in range(len(nums)):
            while used & nums[end]:
                used = used ^ nums[start]
                start += 1

            used = used | nums[end]
            longest = max(longest, end - start + 1)

        return longest

print(Solution().longestNiceSubarray([1,3,8,48,10]))
print(Solution().longestNiceSubarray([3,1,5,11,13]))
