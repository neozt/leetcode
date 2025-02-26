from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        most_positive = 0
        most_negative = 0
        result = 0
        for num in nums:
            most_positive = max(0, most_positive + num)
            most_negative = min(0, most_negative + num)

            result = max(result, most_positive, -most_negative)

        return result

print(Solution().maxAbsoluteSum([1,-3,2,3,-4]))
print(Solution().maxAbsoluteSum([2,-5,1,-4,3,-2]))
