from typing import List


class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        ans = 0
        if len(nums1) % 2 != 0:
            for num in nums2:
                ans = ans ^ num

        if len(nums2) % 2 != 0:
            for num in nums1:
                ans = ans ^ num

        return ans


print(Solution().xorAllNums([2, 1, 3], [10, 2, 5, 0]))
print(Solution().xorAllNums([1, 2], [3, 4]))
