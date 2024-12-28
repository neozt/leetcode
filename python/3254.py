from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        result = []
        consecutive_count = 0
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] + 1:
                consecutive_count += 1
            else:
                consecutive_count = 1

            if i >= k - 1:
                if consecutive_count >= k:
                    result.append(nums[i])
                else:
                    result.append(-1)

        return result


print(Solution().resultsArray([1,2,3,4,3,2,5], 3))
print(Solution().resultsArray([2,2,2,2,2], 4))
print(Solution().resultsArray([3,2,3,2,3,2], 2))
print(Solution().resultsArray([1,4,3,2,5,2,5], 5))