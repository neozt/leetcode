from collections import deque
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        mini, maxi, start = -1, -1, -1
        result = 0

        for i, num in enumerate(nums):
            if num < minK or num > maxK:
                mini, maxi, start = -1, -1, i
                continue

            if num == minK:
                mini = i

            if num == maxK:
                maxi = i

            if mini != -1 and maxi != -1:
                s = min(mini, maxi)
                result += s - start

        return result


print(Solution().countSubarrays([1,3,5,2,7,5], 1, 5))
print(Solution().countSubarrays([1,1,1,1], 1, 1))
print(Solution().countSubarrays([4,3], 3, 3))

