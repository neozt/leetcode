from typing import List


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        largest_multiplier = [0] * len(nums)
        largest = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            largest_multiplier[i] = largest
            largest = max(largest, nums[i])

        best = 0
        largest = nums[0]
        for i in range(1, len(nums) - 1):
            best = max(best, (largest - nums[i]) * largest_multiplier[i])
            largest = max(largest, nums[i])

        return best

print(Solution().maximumTripletValue([12,6,1,2,7]))
print(Solution().maximumTripletValue([1,10,3,4,19]))
print(Solution().maximumTripletValue([1,2,3]))
