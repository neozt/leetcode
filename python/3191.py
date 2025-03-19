from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        flips = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                flips += 1
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1

        if nums[-1] == 1 and nums[-2] == 1:
            return flips

        return -1

print(Solution().minOperations([0,1,1,1,0,0]))
print(Solution().minOperations([0,1,1,1]))
