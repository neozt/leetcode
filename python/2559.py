from typing import List


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        prefix_sum = [0] * (n + 1) # Let prefix_sum[i] = number of words up to i (exclusive) in words array that start and end with a vowel

        for i in range(n):
            word = words[i]
            if is_vowel(word[0]) and is_vowel(word[-1]):
                prefix_sum[i + 1] = prefix_sum[i] + 1
            else:
                prefix_sum[i + 1] = prefix_sum[i]

        return [prefix_sum[r + 1] - prefix_sum[l] for l, r in queries]

def is_vowel(ch):
    return ch in 'aeiou'


print(Solution().vowelStrings(["aba","bcb","ece","aa","e"], [[0,2],[1,4],[1,1]]))
print(Solution().vowelStrings(["a","e","i"], [[0,2],[0,1],[2,2]]))
