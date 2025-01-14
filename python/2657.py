from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_a = set()
        seen_b = set()

        result = []
        for a, b in zip(A, B):
            seen_a.add(a)
            seen_b.add(b)
            result.append(len(seen_a.intersection(seen_b)))

        return result

print(Solution().findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))
print(Solution().findThePrefixCommonArray([2,3,1], [3,1,2]))
