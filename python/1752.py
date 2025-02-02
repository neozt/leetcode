from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        reset_count = 0
        for i in range(0, len(nums)):
            if nums[i] < nums[(i - 1) % len(nums)]:
                reset_count += 1
                if reset_count > 1:
                    return False

        return True

print(Solution().check([3,4,5,1,2]))
print(Solution().check([2,1,3,4]))
print(Solution().check([1,2,3]))

