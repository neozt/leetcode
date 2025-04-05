from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def backtrack(index: int, accumulator: int):
            if index == len(nums):
                return accumulator

            return backtrack(index + 1, accumulator) + backtrack(index + 1, accumulator ^ nums[index])

        return backtrack(0, 0)


print(Solution().subsetXORSum([1,3]))
print(Solution().subsetXORSum([5,1,6]))
print(Solution().subsetXORSum([3,4,5,6,7,8]))
