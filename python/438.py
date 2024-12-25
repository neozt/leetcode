from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        diff = Counter(p)

        result = []
        start, end = 0, len(p) - 1
        for i in range(start, end + 1):
            diff[s[i]] = diff.get(s[i], 0) - 1

        while end < len(s):
            if all(count == 0 for count in diff.values()):
                result.append(start)

            diff[s[start]] += 1
            start += 1
            end += 1
            if end < len(s):
                diff[s[end]] = diff.get(s[end], 0) - 1

        return result


print(Solution().findAnagrams("cbaebabacd", 'abc'))
print(Solution().findAnagrams("abab", 'ab'))

