class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False

            n = n // 3

        return True

print(Solution().checkPowersOfThree(12))
print(Solution().checkPowersOfThree(91))
print(Solution().checkPowersOfThree(21))
