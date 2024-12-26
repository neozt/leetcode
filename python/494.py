from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return helper(nums, target, 0, {})

def helper(nums, target, index, memo):
    if index >= len(nums):
        if target == 0:
            return 1
        else:
            return 0

    if (target, index) in memo:
        return memo[(target, index)]

    current  = nums[index]

    answer = helper(nums, target - current, index + 1, memo) + helper(nums, target + current, index + 1, memo)
    memo[(target, index)] = answer
    return answer

print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
print(Solution().findTargetSumWays([1], 1))
