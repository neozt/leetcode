import math
from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        current_group = self.countSetBits(nums[0])
        current_group_max = nums[0]
        previous_group_max = -math.inf
        for i in range(1, len(nums)):
            current = nums[i]
            next_group = self.countSetBits(current)
            if next_group != current_group:
                previous_group_max = current_group_max
                current_group = next_group
                current_group_max = current

            if current < previous_group_max:
                return False

            current_group_max = max(current_group_max, current)

        return True

    def countSetBits(self, n):
        count = 0
        while n:
            if n & 1:
                count += 1
            n = n >> 1
        return count

print(Solution().canSortArray([8,4,2,30,15]))
print(Solution().canSortArray([1,2,3,4,5]))
print(Solution().canSortArray([3,16,8,4,2]))
