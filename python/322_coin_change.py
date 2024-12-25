import math
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                j = i + coin
                if j > amount:
                    continue
                dp[j] = min(dp[j], dp[i] + 1)

        return dp[amount] if not math.isinf(dp[amount]) else -1


print(Solution().coinChange([1, 2, 5], 10))
print(Solution().coinChange([2], 3))
print(Solution().coinChange([1, 2, 5], 0))
