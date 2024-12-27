import math
from typing import List


class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # score = (values[i] + i) + (values[j] - j)
        # we use m to keep track of best values[i] + i seen so far
        best = values[0]
        m = values[0]

        for i in range (1, len(values)):
            best = max(best, m + values[i] - i)
            m = max(m, values[i] + i)

        return best

print(Solution().maxScoreSightseeingPair([8,1,5,2,6]))
print(Solution().maxScoreSightseeingPair([1,2]))
