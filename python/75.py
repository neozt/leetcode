from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # Dutch national flag algorithm
        left, middle, right = 0, 0, len(nums) - 1

        while middle <= right:
            if nums[middle] == 0:
                # Swap left and middle
                nums[left], nums[middle] = nums[middle], nums[left]
                left += 1
                middle += 1
            elif nums[middle] == 1:
                middle += 1
            else:
                # Swap middle and right
                nums[right], nums[middle] = nums[middle], nums[right]
                right -= 1



input1 = [2,0,2,1,1,0]
Solution().sortColors(input1)
print(input1)

input2 = [2,0,1]
Solution().sortColors(input2)
print(input2)