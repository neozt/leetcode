from collections import deque
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        nums_sorted = sorted(nums)
        nums_to_group = {nums_sorted[0]: 0}
        groups = [deque([nums_sorted[0]])]

        for i in range(1, len(nums_sorted)):
            if nums_sorted[i] - nums_sorted[i - 1] > limit:
                groups.append(deque())

            nums_to_group[nums_sorted[i]] = len(groups) - 1
            groups[-1].append(nums_sorted[i])

        result = []
        for num in nums:
            # Replace with smallest element from same group
            group = nums_to_group[num]
            result.append(groups[group].popleft())

        return result

print(Solution().lexicographicallySmallestArray([1,5,3,9,8], 2))
print(Solution().lexicographicallySmallestArray([1,7,6,18,2,1], 3))
print(Solution().lexicographicallySmallestArray([1,7,28,19,10], 3))
