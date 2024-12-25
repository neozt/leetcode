class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_i = 0
        t_i = 0

        while s_i < len(s) and t_i < len(t):
            if s[s_i] == t[t_i]:
                t_i += 1

            s_i += 1

        return len(t) - t_i


print(Solution().appendCharacters('coaching', 'coding'))
print(Solution().appendCharacters('abcde', 'a'))
print(Solution().appendCharacters('z', 'abcde'))
