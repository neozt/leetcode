import heapq
from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        i = 0
        while nums[0] < k:
            x = heapq.heappop(nums)
            y = heapq.heappop(nums)
            heapq.heappush(nums, min(x, y) * 2 + max(x, y))
            i += 1

        return i

print(Solution().minOperations([2,11,10,1,3], 10))
print(Solution().minOperations([1,1,2,4,9], 20))
