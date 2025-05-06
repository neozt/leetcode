from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] + (nums[nums[i]] % 1000) * 1000

        for i in range(len(nums)):
            nums[i] = nums[i] // 1000

        return nums

print(Solution().buildArray([0,2,1,5,3,4]))
print(Solution().buildArray([5,0,1,2,3,4]))
