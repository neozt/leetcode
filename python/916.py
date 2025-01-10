from collections import Counter
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        required_count_map = Counter()
        for word in words2:
            counter = Counter(word)
            for ch, count in counter.items():
                required_count_map[ch] = max(required_count_map[ch], count)

        return [word for word in words1 if is_universal(word, required_count_map)]

def is_universal(s: str, required_count_map) -> bool:
    char_count = Counter(s)
    for ch, required_count in required_count_map.items():
        if required_count > char_count[ch]:
            return False

    return True


print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","o"]))
print(Solution().wordSubsets(["amazon","apple","facebook","google","leetcode"], ["e","l"]))
