class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        if not s or maxCost < 0:
            return 0

        exclude_self = self.equalSubstring(s[1:], t[1:], maxCost)
        best = exclude_self

        difference = abs(ord(s[0]) - ord(t[0]))
        if difference <= maxCost:
            include_self = self.equalSubstring(s[1:], t[1:], maxCost - difference) + 1
            best = max(best, include_self)

        return best


0, 0, 3
1, 1, 2
2, 2, 1
3, 3, 0

print(Solution().equalSubstring('abcd', 'bcdf', 3))
print(Solution().equalSubstring('abcd', 'cdef', 3))
print(Solution().equalSubstring('abcd', 'acde', 0))
print(Solution().equalSubstring('abcd', 'acde', 0))
