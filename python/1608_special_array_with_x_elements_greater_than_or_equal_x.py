import bisect
from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums = sorted(nums)
        x_arr = [len(nums) - bisect.bisect_left(nums, i) for i in range(0, len(nums) + 1)]

        x_arr.index()
        for i, x in enumerate(x_arr):
            if i == x:
                return i
        return -1


print(Solution().specialArray([3, 5]))
print(Solution().specialArray([0, 0]))
print(Solution().specialArray([0, 4, 3, 0, 4]))
