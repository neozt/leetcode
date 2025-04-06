from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()

        def backtrack(index: int, current_path: List[int]) -> List[int]:
            if index == len(nums):
                return current_path.copy()

            skip = backtrack(index + 1, current_path)
            take = []
            if len(current_path) == 0 or nums[index] % current_path[-1] == 0:
                current_path.append(nums[index])
                take = backtrack(index + 1, current_path)
                current_path.pop()

            return skip if len(skip) > len(take) else take

        return backtrack(0, [])

print(Solution().largestDivisibleSubset([1,2,3]))
print(Solution().largestDivisibleSubset([1,2,4,8]))
