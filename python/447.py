from collections import defaultdict, Counter
from typing import List


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        point_to_counter = defaultdict(Counter)

        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]

                delta_x = p1[0] - p2[0]
                delta_y = p1[1] - p2[1]
                distance = delta_x * delta_x + delta_y * delta_y # Omit square root as we are only interested in the relative magnitude

                point_to_counter[(p1[0], p1[1])][distance] += 1
                point_to_counter[(p2[0], p2[1])][distance] += 1


        result = 0
        for counter in point_to_counter.values():
            for freq in counter.values():
                result += freq * (freq - 1)

        return result


print(Solution().numberOfBoomerangs([[0,0],[1,0],[2,0]]))
print(Solution().numberOfBoomerangs([[1,1],[2,2],[3,3]]))
print(Solution().numberOfBoomerangs([[1,1]]))
