class Solution:
    MOD = 10 ** 9 + 7

    def countGoodNumbers(self, n: int) -> int:
        evens = (n // 2) + (1 if n % 2 != 0 else 0)
        odds = n // 2

        return (self.fast_exponentiation(5, evens) * self.fast_exponentiation(4, odds)) % self.MOD

    def fast_exponentiation(self, x: int, n: int):
        ret, mul = 1, x
        while n > 0:
            if n & 1:
                ret = ret * mul % self.MOD
            mul = mul * mul % self.MOD
            n = n //2
        return ret


print(Solution().countGoodNumbers(1))
print(Solution().countGoodNumbers(4))
print(Solution().countGoodNumbers(50))
# print(Solution().countGoodNumbers(806166225460393))
