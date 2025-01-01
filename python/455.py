from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        j = 0

        satisfied = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
                j += 1
                satisfied += 1

            else:
                j += 1

        return satisfied

assert Solution().findContentChildren([1,2,3], [1,1]) == 1
assert Solution().findContentChildren([1,2], [1,2,3]) == 2
