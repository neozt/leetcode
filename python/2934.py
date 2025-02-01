from typing import List


class Solution:
    def _minOperations(self, nums1, nums2, last1, last2):
        swaps = 0
        for n1, n2 in zip(nums1, nums2):
            if n1 <= last1 and n2 <= last2:
                pass
            elif n1 <= last2 and n2 <= last1:
                swaps += 1
            else:
                return -1

        return swaps

    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        return min(
            self._minOperations(nums1[:-1], nums2[:-1], nums1[-1], nums2[-1]),
            self._minOperations(nums1[:-1], nums2[:-1], nums2[-1], nums1[-1]) + 1
        )

print(Solution().minOperations([1,2,7], [4,5,3]))
print(Solution().minOperations([2,3,4,5,9], [8,8,4,4,4]))
print(Solution().minOperations([1,5,4], [2,5,3]))
