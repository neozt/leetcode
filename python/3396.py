from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        distinct_elements = set()
        operations = 0
        truncated_start = 0
        i = 0
        while i < len(nums):
            while nums[i] in distinct_elements:
                for j in range(3):
                    if truncated_start + j >= i:
                        break
                    distinct_elements.remove(nums[truncated_start + j])
                truncated_start += 3
                operations += 1

            if truncated_start > i:
                i = truncated_start
            else:
                distinct_elements.add(nums[i])
                i += 1

        return operations

print(Solution().minimumOperations([1,2,3,4,2,3,3,5,7]))
print(Solution().minimumOperations([4,5,6,4,4]))
print(Solution().minimumOperations([6,7,8,9]))
print(Solution().minimumOperations([8,8,11,8]))
