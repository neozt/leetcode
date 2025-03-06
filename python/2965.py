from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        duplicate = -1
        missing = -1

        for row in grid:
            for num in row:
                if num in seen:
                    duplicate = num

                seen.add(num)


        for i in range(1, len(grid) * len(grid) + 1):
            if i not in seen:
                missing = i
                break

        return [duplicate, missing]

print(Solution().findMissingAndRepeatedValues([[1,3],[2,2]]))
print(Solution().findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))
