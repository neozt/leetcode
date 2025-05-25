from collections import Counter
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        freq = Counter()
        result = 0
        for word in words:
            pair = word[1] + word[0]
            if freq[pair] > 0:
                result += 4
                freq[pair] -= 1
            else:
                freq[word] += 1

        for word, count in freq.items():
            if count > 0 and word[0] == word[1]:
                result += 2
                break

        return result


print(Solution().longestPalindrome(["lc","cl","gg"]))
print(Solution().longestPalindrome(["ab","ty","yt","lc","cl","ab"]))
print(Solution().longestPalindrome(["cc","ll","xx"]))
