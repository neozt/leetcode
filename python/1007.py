import math
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        candidates = {tops[0], bottoms[0]}

        for i in range(1, len(tops)):
            for candidate in list(candidates):
                if not (tops[i] == candidate or bottoms[i] == candidate):
                    candidates.remove(candidate)

        if not candidates:
            return -1

        min_swaps = math.inf

        for candidate in candidates:
            top_count = bottom_count = 0
            for top, bottom in zip(tops, bottoms):
                if top == candidate:
                    top_count += 1
                if bottom == candidate:
                    bottom_count += 1

            min_swaps = min(min_swaps, len(tops) - max(top_count, bottom_count))

        return min_swaps

print(Solution().minDominoRotations([2,1,2,4,2,2], [5,2,6,2,3,2]))
print(Solution().minDominoRotations([3,5,1,2,3], [3,6,3,3,4]))
