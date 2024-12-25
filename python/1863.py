from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.subsetXOR(nums, 0, 0)

    def subsetXOR(self, nums: List[int], i, currentXor):
        if i >= len(nums):
            return currentXor

        include = self.subsetXOR(nums, i + 1, currentXor ^ nums[i])
        exclude = self.subsetXOR(nums, i + 1, currentXor)

        return include + exclude


print(Solution().subsetXORSum([1, 3]))
print(Solution().subsetXORSum([5,1,6]))
print(Solution().subsetXORSum([3,4,5,6,7,8]))
