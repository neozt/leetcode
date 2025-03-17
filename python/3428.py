import math
from typing import List

# TODO TLE
class Solution:
    def minMaxSums(self, nums: List[int], k: int) -> int:
        def helper(i: int, maximum: int | float, minimum: int | float, used: int) -> int:
            if i == len(nums):
                ret = 0
                if not math.isinf(maximum):
                    ret += maximum
                if not math.isinf(minimum):
                    ret += minimum
                return ret

            ret2 = helper(i + 1, maximum, minimum, used) # Option 1: Skip nums[i]
            if used < k:
                ret2 = (ret2 + helper(i + 1, max(maximum, nums[i]), min(minimum, nums[i]), used + 1)) % (10 ** 9 + 7) # Option 2: Include nums[i]

            return ret2

        return helper(0, -math.inf, math.inf, 0)

print(Solution().minMaxSums([1,2,3], 2))
print(Solution().minMaxSums([5,0,6], 1))
print(Solution().minMaxSums([1,1,1], 2))