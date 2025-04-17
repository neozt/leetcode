from typing import List


class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        result = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if (i * j) % k == 0:
                    if nums[i] == nums[j]:
                        result += 1

        return result


print(Solution().countPairs([3,1,2,2,2,1,3], 2))
print(Solution().countPairs([1,2,3,4], 1))
