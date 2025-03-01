from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        result_index = 0

        for i in range(len(nums) - 1):
            if nums[i] == 0:
                continue

            if nums[i] == nums[i + 1]:
                nums[result_index] = 2 * nums[i]
                nums[i + 1] = 0
            else:
                nums[result_index] = nums[i]
            result_index += 1

        nums[result_index] = nums[-1]
        result_index += 1

        while result_index < len(nums):
            nums[result_index] = 0
            result_index += 1

        return nums


print(Solution().applyOperations([1,2,2,1,1,0]))
print(Solution().applyOperations([0,1]))
