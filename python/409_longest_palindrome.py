class Solution:
    def longestPalindrome(self, s: str) -> int:
        result = 0

        prev = [False] * (ord('z') - ord('A') + 1)

        for ch in s:
            if prev[ord(ch) - ord('A')]:
                result += 2
            prev[ord(ch) - ord('A')] = not prev[ord(ch) - ord('A')]

        if any(prev):
            result += 1

        return result


print(Solution().longestPalindrome("abccccdd"))
print(Solution().longestPalindrome("a"))

print(ord('a'))
print(ord('z') - ord('A'))
print(ord('A'))
print(ord('Z'))
