from collections import defaultdict
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique_nums = set()
        counter1 = defaultdict(int)
        counter2 = defaultdict(int)
        for n in nums1:
            counter1[n] += 1
            unique_nums.add(n)
        for n in nums2:
            counter2[n] += 1
            unique_nums.add(n)

        result = []
        for n in unique_nums:
            count = min(counter1[n], counter2[n])
            for i in range(count):
                result.append(n)

        return result

    def intersect2(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        result = []
        i = 0
        j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                i += 1
        return result

print(Solution().intersect2([1,2,2,1], [2,2]))
print(Solution().intersect2([4,9,5], [9,4,9,8,4]))

