from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        # j - i != nums[j] - nums[i]
        # => j != nums[j] - nums[i] + i
        # => j - nums[j] != i - nums[i]
        result = 0
        total = 0
        freq = defaultdict(int) # stores count of (i - nums[i])
        for i in range(len(nums)):
            result += total - freq[i - nums[i]]
            freq[i - nums[i]] += 1
            total += 1

        return result

print(Solution().countBadPairs([4,1,3,3]))
print(Solution().countBadPairs([1,2,3,4,5]))
