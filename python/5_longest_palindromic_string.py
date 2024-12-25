class Solution:
    def longestPalindrome(self, s: str) -> str:
        best = ""
        for i in range(len(s)):
            start = end = i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start + 1 > len(best):
                    best = s[start:end + 1]
                start -= 1
                end += 1

        for i in range(len(s) - 1):
            start = i
            end = i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                if end - start + 1 > len(best):
                    best = s[start:end + 1]
                start -= 1
                end += 1

        return best


print((Solution().longestPalindrome("babad")))
print(Solution().longestPalindrome("cbbd"))
print(Solution().longestPalindrome("bb"))
