from collections import defaultdict
from typing import List


class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        visited = defaultdict(int)
        def explore(i):
            if i == len(nums):
                return 1

            # At index i, we have two choices:
            # a. we include nums[i] in the subset (Subject to constraint that nums[i] +- k is not already in the subset)
            # b. or we choose to skip nums[i]

            include_current = 0
            current = nums[i]
            if visited[current-k] == 0 and visited[current+k] == 0:
                # Include current
                visited[current] += 1
                include_current = explore(i + 1)
                visited[current] -= 1

            # Exclude current
            exclude_current = explore(i + 1)

            return include_current + exclude_current

        return explore(0) - 1

print(Solution().beautifulSubsets([2, 4, 6], 2))
print(Solution().beautifulSubsets([1], 2))
print(Solution().beautifulSubsets([4,2,5,9,10,3], 1))
