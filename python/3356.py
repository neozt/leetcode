from typing import List


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        left = 0
        right = len(queries)

        if not can_make_zero_array(nums, queries, len(queries)):
            return -1

        while left < right:
            mid = (left + right) // 2

            if can_make_zero_array(nums, queries, mid):
                right = mid
            else:
                left = mid + 1

        return left

def can_make_zero_array(nums: List[int], queries: List[List[int]], k: int) -> bool:
    difference_array = [0] * (len(nums) + 1)
    for i in range(k):
        l, r, val = queries[i]
        difference_array[l] += val
        difference_array[r + 1] -= val

    current_diff = 0
    for i in range(len(nums)):
        current_diff += difference_array[i]
        if nums[i] > current_diff:
            return False

    return True

print(Solution().minZeroArray([2,0,2], [[0,2,1],[0,2,1],[1,1,3]]))
print(Solution().minZeroArray([4,3,2,1], [[1,3,2],[0,2,1]]))
print(Solution().minZeroArray([7,6,8], [[0,0,2],[0,1,5],[2,2,5],[0,2,4]]))
