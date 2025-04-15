from typing import List


class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)

        num_to_pos = {}
        for i, num in enumerate(nums2):
            num_to_pos[num] = i

        result = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    x, y, z = nums1[i], nums1[j], nums1[k]
                    if num_to_pos[x] < num_to_pos[y] < num_to_pos[z]:
                        result += 1

        return result

print(Solution().goodTriplets([2,0,1,3], [0,1,2,3])) # 1
print(Solution().goodTriplets([4,0,1,3,2], [4,1,0,2,3])) # 4
