from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def at_least_k_stealable_houses(threshold: int):
            i = 0
            stealable_houses = 0
            while i < len(nums):
                if nums[i] <= threshold:
                    stealable_houses += 1
                    if stealable_houses == k:
                        return True
                    i += 2
                else:
                    i += 1

            return False


        left = 0
        right = max(nums)

        while left < right:
            mid = (left + right) // 2

            if at_least_k_stealable_houses(mid):
                right = mid
            else:
                left = mid + 1

        return left




print(Solution().minCapability([2,3,5,9], 2))
print(Solution().minCapability([2,7,9,3,1], 2))


