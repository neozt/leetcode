class Solution:
    def numSteps(self, s: str) -> int:
        def helper(n: int) -> int:
            if n == 1:
                return 0

            if n % 2 == 0:
                return helper(n // 2) + 1
            else:
                return helper(n + 1) + 1

        return helper(int(s, 2))


print(Solution().numSteps("1111011110000011100000110001011011110010111001010111110001"))