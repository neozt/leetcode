from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            is_sorted = True

            for j in range(1, len(nums)):
                idx = (i + j) % len(nums)
                if nums[idx] < nums[idx - 1]:
                    is_sorted = False
                    break

            if is_sorted:
                return True

        return False

print(Solution().check([3,4,5,1,2]))
print(Solution().check([2,1,3,4]))
print(Solution().check([1,2,3]))

