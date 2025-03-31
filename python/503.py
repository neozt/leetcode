from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        result = [-1] * len(nums)
        decreasing_stack = []
        for i in range(len(nums) * 2):
            i_mod = i % len(nums)
            while decreasing_stack and nums[decreasing_stack[-1]] < nums[i_mod]:
                prev = decreasing_stack.pop()
                result[prev] = nums[i_mod % len(nums)]
            decreasing_stack.append(i_mod)

        return result



print(Solution().nextGreaterElements([1,2,1]))
print(Solution().nextGreaterElements([1,2,3,4,3]))
