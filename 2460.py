from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result = []
        zeroes = 0

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

            if nums[i] == 0:
                zeroes += 1
            else:
                result.append(nums[i])

        return result + [nums[-1]] + [0] * zeroes


print(Solution().applyOperations([1,2,2,1,1,0]))
print(Solution().applyOperations([0,1]))
