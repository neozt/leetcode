from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = end = 0
        longest = 0
        zero_count = 0

        while end < len(nums):
            if nums[end] == 0:
                zero_count += 1

            while zero_count > k:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1

            longest = max(longest, end - start + 1)
            end += 1

        return longest


print(Solution().longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))
print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
