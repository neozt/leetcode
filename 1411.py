class Solution:
    def maxScore(self, s: str) -> int:
        ones = s.count('1')
        zeroes = 0
        best = 0
        for ch in s[:-1]:
            if ch == '0':
                zeroes += 1
            elif ch == '1':
                ones -= 1

            best = max(best, zeroes + ones)

        return best


print(Solution().maxScore("011101"))
print(Solution().maxScore("00111"))
print(Solution().maxScore("1111"))
print(Solution().maxScore("00"))
