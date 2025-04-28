from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        result = 0

        prefix = [0]
        acc = 0
        for num in nums:
            acc += num
            prefix.append(acc)

        for i in range(len(nums)):
            if nums[i] >= k:
                continue

            left = i
            right = len(nums) - 1
            while left < right:
                middle = (left + right + 1) // 2
                score = (prefix[middle + 1] - prefix[i]) * (middle - i + 1)

                if score >= k:
                    right = middle - 1
                else:
                    left = middle

            result += left - i + 1

        return result

print(Solution().countSubarrays([2,1,4,3,5], 10))
print(Solution().countSubarrays([1,1,1], 5))
