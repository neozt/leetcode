from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greatest = {}

        decreasing_stack = []
        for i, num in enumerate(nums2):
            while decreasing_stack and decreasing_stack[-1] < num:
                prev = decreasing_stack.pop()
                next_greatest[prev] = num
            decreasing_stack.append(num)

        result = []
        for num in nums1:
            result.append(next_greatest.get(num, -1))

        return result


print(Solution().nextGreaterElement([4,1,2], [1,3,4,2]))
print(Solution().nextGreaterElement([2,4], [1,2,3,4]))
