from collections import defaultdict
from typing import List


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        count = [0] * n
        for city1, city2 in roads:
            count[city1] += 1
            count[city2] += 1

        frequencies = sorted(count)
        result = 0
        for i, freq in enumerate(frequencies):
            result += (i + 1) * freq

        return result


print(Solution().maximumImportance(5, [[0, 1], [1, 2], [2, 3], [0, 2], [1, 3], [2, 4]]))
print(Solution().maximumImportance(5, [[0,3],[2,4],[1,3]]))