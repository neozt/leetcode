class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        return self.helper(n, k, target, {})

    def helper(self, n: int, k: int, target: int, memo) -> int:
        if n == 0 and target == 0:
            return 1

        if target == 0 or n == 0:
            return 0

        if (n, k, target) not in memo:
            memo[(n, k, target)] = sum(self.helper(n - 1, k, target - i, memo) for i in range(1, k + 1)) % (10 ** 9 + 7)

        return memo[(n, k, target)]


print(Solution().numRollsToTarget(1, 6, 3))
print(Solution().numRollsToTarget(2, 6, 7))
print(Solution().numRollsToTarget(30, 30, 500))
