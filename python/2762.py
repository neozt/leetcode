import math
from collections import Counter
from typing import List


class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        freq = Counter()
        start = 0
        end = 0
        result = 0
        while end < len(nums):
            freq[end] += 1
            if get_count(freq, nums[end]) == (end - start):
                result += 1
                end += 1
            else:
                freq[start] -= 1
                start += 1

def get_count(freq, n):
    return freq[n] + freq[n + 1] + freq[n + 2] + freq[n-1] + freq[n-2]

print(Solution().continuousSubarrays([5,4,2,4]))
# 5 5,4 5,4,2 5,4,2,4
# 4