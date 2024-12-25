from typing import List

class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            if nums[middle] == target:
                return middle

            # This algorithm exploits the fact that one of the half, either left or right of the array must be correctly sorted
            # Left half is sorted
            if nums[left] <= nums[middle]:
                # Check which half target resides in
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            # Right half is sorted
            else:
                # Check which half target resides in
                if nums[middle] < target <= nums[right]:
                    left = middle + 1
                else:
                    right = middle - 1

        return -1


# print(Solution().search([0,1,2,4,5,6,7], 0))
print(Solution().search([4,5,6,7,0,1,2], 0))
print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([1], 0))
print(Solution().search([3,1], 1))
# print(Solution().search([3,5,1], 5))

