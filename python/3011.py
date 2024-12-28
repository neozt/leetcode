import math
from typing import List


class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        current_group = nums[0].bit_count()
        current_group_max = nums[0]
        previous_group_max = -math.inf
        for i in range(1, len(nums)):
            current = nums[i]
            next_group = current.bit_count()
            if next_group != current_group:
                previous_group_max = current_group_max
                current_group = next_group
                current_group_max = current

            if current < previous_group_max:
                return False

            current_group_max = max(current_group_max, current)

        return True

print(Solution().canSortArray([8,4,2,30,15]))
print(Solution().canSortArray([1,2,3,4,5]))
print(Solution().canSortArray([3,16,8,4,2]))
