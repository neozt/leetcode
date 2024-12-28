from collections import deque, Counter
from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = []
        for i, n in enumerate(nums):
            if i < k - 1:
                continue

            is_valid = True
            for j in range(0, k):
                el = nums[i - k + j + 1]
                if el != n - k + j + 1:
                    is_valid = False
                    break

            if is_valid:
                result.append(n)
            else:
                result.append(-1)

        return result


print(Solution().resultsArray([1,2,3,4,3,2,5], 3))
print(Solution().resultsArray([2,2,2,2,2], 4))
print(Solution().resultsArray([3,2,3,2,3,2], 2))
print(Solution().resultsArray([1,4,3,2,5,2,5], 5))