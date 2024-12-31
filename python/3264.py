import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, i) for (i, num) in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            (minimum, index) = heapq.heappop(heap)
            heapq.heappush(heap, (minimum * multiplier, index))

        result = [0 for i in range(len(nums))]

        for (n, i) in heap:
            result[i] = n

        return result
