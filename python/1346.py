from typing import List


class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for n in arr:
            if n * 2 in seen:
                return True

            if (n % 2 == 0 and n / 2 in seen):
                return True

            seen.add(n)

        return False


# print(Solution().checkIfExist([10,2,5,3]))
# print(Solution().checkIfExist([3,1,7,11]))
a = [-2,0,10,-19,4,6,-8]
print(Solution().checkIfExist(a))