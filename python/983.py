from functools import cache
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        @cache
        def helper(index: int, covered_until: int) -> int:
            if index >= len(days):
                return 0

            next = days[index]
            if next <= covered_until:
                return helper(index + 1, covered_until)

            return min(
                helper(index + 1, next) + costs[0],
                helper(index + 1, next + 6) + costs[1],
                helper(index + 1, next + 29) + costs[2],
            )

        return helper(0, 0)


print(Solution().mincostTickets([1,4,6,7,8,20], [2,7,15]))
print(Solution().mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]))
