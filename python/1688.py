class Solution:
    def numberOfMatches(self, n: int) -> int:
        result = 0
        while n > 1:
            half = n // 2
            result += half
            if n % 2 == 0:
                n = half
            else:
                n = half + 1

        return result

print(Solution().numberOfMatches(7))
print(Solution().numberOfMatches(14))
