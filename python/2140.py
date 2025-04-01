from typing import List


class Solution:
    # Bottom up DP
    # Time: O(N)
    # Space: O(N)
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0] * len(questions)
        for i in reversed(range(len(questions))):
            points, brainpower = questions[i]
            dp[i] = max(
                dp[i + 1] if i + 1 < len(questions) else 0,
                points + (dp[i + brainpower + 1] if i + brainpower + 1 < len(questions) else 0)
            )

        return dp[0]


print(Solution().mostPoints([[3,2],[4,3],[4,4],[2,5]]))
print(Solution().mostPoints([[1,1],[2,2],[3,3],[4,4],[5,5]]))
