from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # j - i != nums[j] - nums[i]
        # => j != nums[j] - nums[i] + i
        # => j - nums[j] != i - nums[i]
        n = len(nums)
        freq = defaultdict(int) # stores count of (i - nums[i])
        good_pairs = 0
        for i in range(len(nums)):
            temp = i - nums[i]
            good_pairs += freq[temp]
            freq[temp] += 1

        total_pairs = (n * (n - 1)) // 2 # 0 + 1 + ... + (n - 1)

        return total_pairs - good_pairs

print(Solution().countBadPairs([4,1,3,3]))
print(Solution().countBadPairs([1,2,3,4,5]))
