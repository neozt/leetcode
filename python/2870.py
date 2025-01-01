import math
from collections import Counter
from functools import cache
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def countOperationsToZero(n):
            if n == 1:
                return math.inf

            return (n // 3) + (1 if n % 3 else 0)

        freq = Counter(nums)
        total = sum(countOperationsToZero(f) for f in freq.values())
        return -1 if math.isinf(total) else total

print(Solution().minOperations([2, 3, 3, 2, 2, 4, 2, 3, 4]))
print(Solution().minOperations([2,1,2,2,3,3]))

