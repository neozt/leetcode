class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False

        pretty_factors = [2, 3, 5]

        for factor in pretty_factors:
            while n % factor == 0:
                n = n // factor

        return n == 1

print(Solution().isUgly(2147483648))