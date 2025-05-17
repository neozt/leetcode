from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_zero = 0
        last_one = 0

        for i, num in enumerate(nums):
            if num == 0:
                nums[i] = 2
                nums[last_one] = 1
                nums[last_zero] = 0
                last_one += 1
                last_zero += 1

            elif num == 1:
                nums[i] = 2
                nums[last_one] = 1
                last_one += 1

            else:
                # do nothing
                pass

print(Solution().sortColors([2,0,2,1,1,0]))
print(Solution().sortColors([2,0,1]))
