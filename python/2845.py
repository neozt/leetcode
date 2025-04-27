from collections import Counter
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        result = 0
        current = 0
        count = Counter({0: 1})
        for i, num in enumerate(nums):
            if num % modulo == k:
                current += 1

            result += count.get((current - k + modulo) % modulo, 0)
            count[current % modulo] += 1

        return result

print(Solution().countInterestingSubarrays([3,2,4],2,1))
print(Solution().countInterestingSubarrays([3,1,9,6],3, 0))
print(Solution().countInterestingSubarrays([11,12,21,31],10,1))


