from collections import deque
from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minQ = deque()
        maxQ = deque()
        left = 0
        result = 0

        for i in range(len(nums)):
            num = nums[i]

            if num < minK or num > maxK:
                minQ.clear()
                maxQ.clear()
                left = i + 1
                continue

            while minQ and num <= nums[minQ[-1]]:
                minQ.pop()
            minQ.append(i)

            while maxQ and num >= nums[maxQ[-1]]:
                maxQ.pop()
            maxQ.append(i)

            if nums[minQ[0]] == minK and nums[maxQ[0]] == maxK:
                start = min(minQ[0], maxQ[0])
                result += start - left + 1

        return result


print(Solution().countSubarrays([1,3,5,2,7,5], 1, 5))
print(Solution().countSubarrays([1,1,1,1], 1, 1))

