from collections import Counter
from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        sorted_nums = sorted(nums)
        start = 0
        end = 0
        best = 0

        k_2 = k * 2

        while end < len(nums):
            if sorted_nums[end] - sorted_nums[start] <= k_2:
                end += 1
            else:
                start += 1

            best = max(best, end - start)

        return best

print(Solution().maximumBeauty([4,6,1,2], 2))
print(Solution().maximumBeauty([1,1,1,1], 10))
print(Solution().maximumBeauty([49,26], 12))
