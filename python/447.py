from collections import defaultdict, Counter
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        result = 0
        for i in range(len(points)):
            freq = defaultdict(int)
            for j in range(len(points)):
                if i == j:
                    continue

                p1 = points[i]
                p2 = points[j]
                dx = p1[0] - p2[0]
                dy = p1[1] - p2[1]

                distance = dx * dx + dy * dy # Omit square root as we are only interested in the relative magnitude
                freq[distance] += 1

            for f in freq.values():
                result += f * (f - 1)

        return result


print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))
print(Solution().numberOfBoomerangs([[1,1],[2,2],[3,3]]))
print(Solution().numberOfBoomerangs([[1,1]]))
