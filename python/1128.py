from collections import Counter
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = Counter()
        total_pairs = 0

        for top, bottom in dominoes:
            if top > bottom:
                domino = (bottom, top)
            else:
                domino = (top, bottom)

            total_pairs += counter[domino]
            counter[domino] += 1

        return total_pairs

print(Solution().numEquivDominoPairs([[1,2],[2,1],[3,4],[5,6]]))
print(Solution().numEquivDominoPairs([[1,2],[1,2],[1,1],[1,2],[2,2]]))
