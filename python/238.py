from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProduct = [1] * (len(nums))
        rightProduct = [1] * (len(nums))

        for i in range(1, len(nums)):
            leftProduct[i] = leftProduct[i - 1] * nums[i - 1]
            rightProduct[-(i + 1)] = rightProduct[-i] * nums[-i]

        return [x * y for (x, y) in zip(leftProduct, rightProduct)]


print(Solution().productExceptSelf([1, 2, 3, 4]))
