import heapq
from typing import List


class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        result = 0
        for i, h in enumerate(happiness[:k]):
            current_happiness = h - i
            if (current_happiness <= 0):
                break
            result += current_happiness

        return result


print(Solution().maximumHappinessSum([1, 2, 3], 2))
print(Solution().maximumHappinessSum([1, 1, 1, 1], 1))
print(Solution().maximumHappinessSum([2,3,4,5], 1))
