import heapq
from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        max_heap = []
        min_heap = []
        for i in range(len(weights) - 1):
            pairwise_sum = weights[i] + weights[i + 1]
            heapq.heappush(min_heap, pairwise_sum)
            heapq.heappush(max_heap, -pairwise_sum)

        maximum = minimum = weights[0] + weights[-1]
        for _ in range(k - 1):
            minimum += heapq.heappop(min_heap)
            maximum += -heapq.heappop(max_heap)

        return maximum - minimum

print(Solution().putMarbles([1,3,5,1], 2))
print(Solution().putMarbles([1,3], 2))
print(Solution().putMarbles([1,4,2,5,2], 3))
