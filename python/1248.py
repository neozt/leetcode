from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        result = 0
        odd_count = [1 if i == 0 else 0 for i in range(len(nums) + 1)]
        current_odd_count = 0

        for num in nums:
            current_odd_count += num & 1

            odd_count[current_odd_count] += 1

            if current_odd_count - k >= 0:
                result += odd_count[current_odd_count - k]

        return result


print(Solution().numberOfSubarrays([1, 1, 2, 1, 1], 3))
print(Solution().numberOfSubarrays([2, 4, 6], 1))
print(Solution().numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], 2))
print(Solution().numberOfSubarrays([2044,96397,50143], 1))