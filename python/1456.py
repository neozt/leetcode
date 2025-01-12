class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        current = sum(is_vowel(ch) for ch in s[:k])
        best = current

        for i in range(1, len(s) - k + 1):
            if is_vowel(s[i-1]):
                current -= 1

            if is_vowel(s[i + k -1]):
                current += 1

            best = max(best, current)

        return best

VOWELS = {'a', 'e', 'i', 'o', 'u'}
def is_vowel(ch: str):
    return ch in VOWELS

print(Solution().maxVowels('abciiidef', 3))
print(Solution().maxVowels('aeiou', 2))
print(Solution().maxVowels('leetcode', 3))
