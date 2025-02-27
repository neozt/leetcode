class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7

        dp = [0] * (high + 1) # dp[i] = number of ways that we can construct an i length string
        dp[0] = 1
        for i in range(1, high + 1):
            if i >= zero:
                dp[i] += dp[i - zero] % MOD
            if i >= one:
                dp[i] += dp[i - one] % MOD

        result = 0
        for i in range(low, high + 1):
            result = (result + dp[i]) % MOD
        return result


print(Solution().countGoodStrings(3, 3, 1 ,1))
print(Solution().countGoodStrings(2, 3, 1, 2))
