from collections import Counter
from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix = [0] * len(nums)

        current = 0
        for i, num in enumerate(nums):
            if num % modulo == k:
                current += 1

            prefix[i] = current


        count = Counter()
        count[0] = 1
        result = 0
        for i, cum in enumerate(prefix):
            result += count.get((cum - k + modulo) % modulo, 0)
            if nums[i] % modulo == k:
                count[cum % modulo] += 1

        return result

print(Solution().countInterestingSubarrays([3,2,4],2,1))
print(Solution().countInterestingSubarrays([3,1,9,6],3, 0))


