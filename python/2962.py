from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maximum = max(nums)

        left = 0
        right = 0
        max_count = 0
        result = 0
        while left < len(nums):
            while right < len(nums) and max_count < k:
                if nums[right] == maximum:
                    max_count += 1
                right += 1

            if max_count != k:
                break

            result += len(nums) - right + 1
            if nums[left] == maximum:
                max_count -= 1
            left += 1

        return result

print(Solution().countSubarrays([1,3,2,3,3], 2))
print(Solution().countSubarrays([1,4,2,1], 3))
