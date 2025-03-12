import bisect
from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        neg = bisect.bisect_left(nums, 0)
        pos = len(nums) - bisect.bisect_right(nums, 0)
        return max(neg, pos)

print(Solution().maximumCount([-2,-1,-1,1,2,3]))
print(Solution().maximumCount([-3,-2,-1,0,0,1,2]))
print(Solution().maximumCount([5,20,66,1314]))
