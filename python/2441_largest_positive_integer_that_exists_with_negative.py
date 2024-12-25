import heapq
from typing import List


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numSet = set(nums)
        heap = nums.copy()
        heapq.heapify(heap)

        while heap:
            currentMin = heapq.heappop(heap)
            if -currentMin in numSet:
                return -currentMin

        return -1


print(Solution().findMaxK([-1,2,-3,3]))
print(Solution().findMaxK([-1,10,6,7,-7,1]))
print(Solution().findMaxK([-10,8,6,7,-2,-3]))
