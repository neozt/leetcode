from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []

        idx1 = idx2 = 0

        while idx1 < len(nums1) or idx2 < len(nums2):
            both_inbounds = idx1 < len(nums1) and idx2 < len(nums2)
            if both_inbounds and nums1[idx1][0] == nums2[idx2][0]:
                result.append([nums1[idx1][0], nums1[idx1][1] + nums2[idx2][1]])
                idx1 += 1
                idx2 += 1
            elif idx2 >= len(nums2) or (both_inbounds and nums1[idx1][0] < nums2[idx2][0]):
                result.append(nums1[idx1])
                idx1 += 1
            else:
                result.append(nums2[idx2])
                idx2 += 1

        return result


print(Solution().mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))
print(Solution().mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]))
