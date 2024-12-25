from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        print(nums)
        for i in range(len(nums) - 2):
            start = i + 1
            end = len(nums) - 1
            while start < end:
                sum = nums[i] + nums[start] + nums[end]
                if sum == 0:
                    result.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif sum < 0:
                    start += 1
                else:
                    end -= 1

        return list(result)


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
