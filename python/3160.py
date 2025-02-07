from collections import defaultdict
from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        freq = defaultdict(int)
        colors = {}
        distinct_colors = 0
        result = []

        for i, color in queries:
            if i in colors:
                prev_color = colors[i]
                freq[prev_color] -= 1
                if freq[prev_color] == 0:
                    distinct_colors -= 1

            colors[i] = color
            freq[color] += 1
            if freq[color] == 1:
                distinct_colors += 1

            result.append(distinct_colors)

        return result

print(Solution().queryResults(4, [[1,4],[2,5],[1,3],[3,4]]))
print(Solution().queryResults(4, [[0,1],[1,2],[2,2],[3,4],[4,5]]))
