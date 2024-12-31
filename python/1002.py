from collections import Counter
from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])
        for i in range(1, len(words)):
            word = words[i]
            count = Counter(word)
            for ch in common:
                common[ch] = min(common[ch], count[ch])

        result = []
        for ch in common:
            for i in range(common[ch]):
                result.append(ch)

        return result


print(Solution().commonChars(["bella", "label", "roller"]))
print(Solution().commonChars(["cool","lock","cook"]))
