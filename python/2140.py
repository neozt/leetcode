from functools import cache
from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        @cache
        def helper(idx: int) -> int:
            if idx >= len(questions):
                return 0

            points, brainpower = questions[idx]
            option1 = points + helper(idx + brainpower + 1)
            option2 = helper(idx + 1)
            return max(
                option1,
                option2
            )

        return helper(0)


print(Solution().mostPoints([[3,2],[4,3],[4,4],[2,5]]))
print(Solution().mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))
