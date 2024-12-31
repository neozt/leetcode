from collections import defaultdict
from typing import List


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        counter = defaultdict(int)
        for u, v in edges:
            counter[u] += 1
            counter[v] += 1
            if (counter[u]) > 2:
                return u
            if (counter[v]) > 2:
                return v

        # Edge case, only 3 nodes
        return next(edge for edge, count in counter.items() if count == 2)
