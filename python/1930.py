class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first_occurrence = {}
        last_occurrence = {}
        for i, ch in enumerate(s):
            if ch not in first_occurrence:
                first_occurrence[ch] = i
            last_occurrence[ch] = i

        palindromes = set()
        for ch, first_occurrence_index in first_occurrence.items():
            last_occurrence_index = last_occurrence[ch]

            for i in range(first_occurrence_index + 1, last_occurrence_index):
                palindromes.add(ch + s[i] + ch)

        return len(palindromes)


print(Solution().countPalindromicSubsequence("aabca"))
print(Solution().countPalindromicSubsequence("adc"))
print(Solution().countPalindromicSubsequence("bbcbaba"))
