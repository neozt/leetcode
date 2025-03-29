import heapq
import math
from functools import cache
from typing import List


# TODO TLE
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        dp = [0] * (max(nums) + 1)
        for i in range(2, len(dp)):
            if dp[i] != 0:
                continue

            j = i
            while j < len(dp):
                dp[j] += 1
                j += i

        max_heap = []
        for i, num in enumerate(nums):
            heapq.heappush(max_heap, (-num, i))

        MOD = 10 ** 9 + 7

        result = 1
        while k > 0:
            best, idx = heapq.heappop(max_heap)
            best = -best
            if best == 1:
                break

            prime_score = dp[best]

            right = idx
            while right < len(nums):
                if dp[nums[right]] > prime_score:
                    break
                right += 1
            after = right - idx

            left = idx - 1
            while left >= 0:
                if dp[nums[left]] >= prime_score:
                    break
                left -= 1

            before = idx - left

            use_count = min(k, after * before)
            k -= use_count
            for i in range(use_count):
                result = (result * best) % MOD

        return result

print(Solution().maximumScore([8,3,9,3,8], 2))
print(Solution().maximumScore([19,12,14,6,10,18], 3))
print(Solution().maximumScore([1,7,11,1,5], 14))
