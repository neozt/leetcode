from collections import deque
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_sorted = sorted(nums)
        nums_to_group = {nums_sorted[0]: 0}
        group_to_nums = [deque([nums_sorted[0]])]

        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] - nums_sorted[i - 1] <= limit:
                # Put into same group
                group = nums_to_group[nums_sorted[i-1]]
                nums_to_group[nums_sorted[i]] = group
                group_to_nums[group].append(nums_sorted[i])

            else:
                # Add new group
                group = nums_to_group[nums_sorted[i-1]] + 1
                nums_to_group[nums_sorted[i]] = group
                group_to_nums.append(deque([nums_sorted[i]]))

        result = []
        for num in nums:
            # Replace with smallest element from same group
            group = nums_to_group[num]
            result.append(group_to_nums[group].popleft())

        return result

print(Solution().lexicographicallySmallestArray([1,5,3,9,8], 2))
print(Solution().lexicographicallySmallestArray([1,7,6,18,2,1], 3))
print(Solution().lexicographicallySmallestArray([1,7,28,19,10], 3))
