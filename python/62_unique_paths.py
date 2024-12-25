class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for i in range(m)]
        dp[m-1][n-1] = 1
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    continue
                paths = 0
                if (i + 1 < m):
                    paths += dp[i+1][j]
                if j + 1 < n:
                    paths += dp[i][j+1]
                dp[i][j] = paths

        return dp[0][0]

print(Solution().uniquePaths(3, 2))
print(Solution().uniquePaths(3, 7))
