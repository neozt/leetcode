from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]

        result = 0
        for i in range(len(nums) - 1):
            right = prefix_sum[-1] - prefix_sum[i]
            if prefix_sum[i] >= right:
                result += 1

        return result

print(Solution().waysToSplitArray([10,4,-8,7]))
print(Solution().waysToSplitArray([2,3,1,0]))
