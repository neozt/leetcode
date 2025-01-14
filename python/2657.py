from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        seen_a = set()
        seen_b = set()
        prev = 0

        result = []
        for a, b in zip(A, B):
            if a == b:
                prev += 1
            else:
                if a in seen_b:
                    prev += 1
                if b in seen_a:
                    prev += 1

            seen_a.add(a)
            seen_b.add(b)

            result.append(prev)

        return result

print(Solution().findThePrefixCommonArray([1,3,2,4], [3,1,2,4]))
print(Solution().findThePrefixCommonArray([2,3,1], [3,1,2]))
