from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        nums = []
        for row in grid:
            for num in row:
                nums.append(num)

        nums.sort()
        median = nums[len(nums) // 2]

        total_operations = 0
        for num in nums:
            diff = abs(num - median)
            if diff % x != 0:
                return -1

            operations = diff // x
            total_operations += operations

        return total_operations

print(Solution().minOperations([[2,4],[6,8]], 2))
print(Solution().minOperations([[1,5],[2,3]], 1))
print(Solution().minOperations([[1,2],[3,4]], 2))
