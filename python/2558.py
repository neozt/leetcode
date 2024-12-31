import heapq
import math
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = [-n for n in gifts]
        heapq.heapify(heap)

        for i in range(k):
            largest_pile = -heapq.heappop(heap)
            left_behind = math.floor(math.sqrt(largest_pile))
            heapq.heappush(heap, -left_behind)

        return -sum(heap)


print(Solution().pickGifts([25,64,9,4,100], 4))
print(Solution().pickGifts([1,1,1,1], 4))
