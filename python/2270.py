from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        result = 0
        for i in range(len(nums) - 1):
            left_sum += nums[i]
            right_sum = total - left_sum
            if left_sum >= right_sum:
                result += 1

        return result

print(Solution().waysToSplitArray([10,4,-8,7]))
print(Solution().waysToSplitArray([2,3,1,0]))
