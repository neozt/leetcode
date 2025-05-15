from typing import List


class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        result = []
        previous_group = None
        for word, group in zip(words, groups):
            if group != previous_group:
                previous_group = group
                result.append(word)

        return result