import math
from collections import Counter
from typing import List


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        freq = Counter()
        current_pairs = 0
        result = 0

        while left < len(nums):
            while current_pairs < k and right < len(nums):
                freq[nums[right]] += 1
                new_freq = freq[nums[right]]
                current_pairs += new_freq - 1
                right += 1

            if current_pairs >= k:
                result += len(nums) - right + 1

                old_freq = freq[nums[left]]
                current_pairs -= old_freq - 1
                freq[nums[left]] -= 1

            left += 1

        return result


def is_good(freq, k):
    pairs = 0
    for f in freq.values():
        pairs += math.comb(f, 2)
    return pairs >= k

print(Solution().countGood([1,1,1,1,1], 10))
print(Solution().countGood([3,1,4,3,2,2,4], 2))
