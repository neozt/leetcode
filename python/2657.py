from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        bitmap_a = 0
        bitmap_b = 0

        result = []
        for a, b in zip(A, B):
            bitmap_a = bitmap_a | (1 << a)
            bitmap_b = bitmap_b | (1 << b)

            result.append((bitmap_a & bitmap_b).bit_count())

        return result

print(Solution().findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))
print(Solution().findThePrefixCommonArray([2,3,1], [3,1,2]))
