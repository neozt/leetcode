from typing import List


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        nums.sort()
        num_tracker = 0
        result = 0
        for num in nums:
            num_tracker = max(num_tracker, num)
            result += num_tracker - num
            num_tracker += 1

        return result


print(Solution().minIncrementForUnique([1, 2, 2]))
print(Solution().minIncrementForUnique([3,2,1,2,1,7]))