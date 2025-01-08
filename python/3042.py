from typing import List


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if isPrefixAndSuffix(words[i], words[j]):
                    result += 1
        return result


def isPrefixAndSuffix(str1: str, str2: str) -> bool:
    return str2.startswith(str1) and str2.endswith(str1)

print(Solution().countPrefixSuffixPairs(["a","aba","ababa","aa"]))
print(Solution().countPrefixSuffixPairs(["pa","papa","ma","mama"]))
print(Solution().countPrefixSuffixPairs(["abab","ab"]))
