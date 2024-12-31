import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(math.floor(math.sqrt(c)) + 1):
            b = math.sqrt(c - a * a)
            if b == int(b):
                return True

        return False


print(Solution().judgeSquareSum(5))
print(Solution().judgeSquareSum(3))
print(Solution().judgeSquareSum(4))
print(Solution().judgeSquareSum(2))
