import heapq
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        capital_profit = list(zip(capital, profits))
        capital_profit.sort(key=lambda x: x[0])
        heap = []
        i = 0
        for _ in range(k):
            while i < len(capital_profit) and capital_profit[i][0] <= w:
                heapq.heappush(heap, -capital_profit[i][1])
                i += 1

            if heap:
                w += -heapq.heappop(heap)

        return w


print(Solution().findMaximizedCapital(2, 0, [1, 2, 3], [0, 1, 1]))
print(Solution().findMaximizedCapital(3, 0, [1, 2, 3], [0, 1, 2]))
print(Solution().findMaximizedCapital(1, 2, [1, 2, 3], [1, 1, 2]))



