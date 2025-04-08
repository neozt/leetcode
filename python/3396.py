from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        array_start = 0
        operations = 0
        i = 0
        distinct_elements = set()
        while i < len(nums):
            while nums[i] in distinct_elements:
                distinct_elements.remove(nums[array_start])
                if array_start + 1 < len(nums) and nums[array_start + 1] in distinct_elements:
                    distinct_elements.remove(nums[array_start + 1])
                if array_start + 2 < len(nums) and nums[array_start + 2] in distinct_elements:
                    distinct_elements.remove(nums[array_start + 2])
                array_start += 3
                operations += 1

            if array_start > i:
                i = array_start
            else:
                distinct_elements.add(nums[i])
                i += 1

        return operations

print(Solution().minimumOperations([1,2,3,4,2,3,3,5,7]))
print(Solution().minimumOperations([4,5,6,4,4]))
print(Solution().minimumOperations([6,7,8,9]))
print(Solution().minimumOperations([8,8,11,8]))
