from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        result = []

        idx1 = idx2 = 0

        while idx1 < len(nums1) or idx2 < len(nums2):
            if (idx1 < len(nums1) and idx2 < len(nums2)):
                if nums1[idx1][0] < nums2[idx2][0]:
                    candidate = nums1[idx1]
                    idx1 += 1
                else:
                    candidate = nums2[idx2]
                    idx2 += 1

            elif idx1 < len(nums1):
                candidate = nums1[idx1]
                idx1 += 1
            else:
                candidate = nums2[idx2]
                idx2 += 1

            if result and result[-1][0] == candidate[0]:
                result[-1] = [result[-1][0], result[-1][1] + candidate[1]]
            else:
                result.append([candidate[0], candidate[1]])

        return result


print(Solution().mergeArrays([[1,2],[2,3],[4,5]], [[1,4],[3,2],[4,1]]))
print(Solution().mergeArrays([[2,4],[3,6],[5,5]], [[1,3],[4,3]]))
