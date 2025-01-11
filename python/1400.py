from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        char_count = Counter(s)
        min_palindromes = 0
        for ch, count in char_count.items():
            if count % 2 != 0:
                min_palindromes += 1

        return min_palindromes <= k

print(Solution().canConstruct("annabelle", 2))
print(Solution().canConstruct("leetcode", 3))
print(Solution().canConstruct("true", 4))
print(Solution().canConstruct("qlkzenwmmnpkopu", 15))
