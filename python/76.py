from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        count = Counter(t)
        start = 0
        end = 0
        best = ""
        counter = len(t)
        while end < len(s):
            if s[end] in count:
                if count[s[end]] > 0:
                    counter -= 1
            count[s[end]] -= 1
            end += 1
            while counter <= 0 and start <= end:
                if not best or (end - start) < len(best):
                    best = s[start:end]

                if count[s[start]] == 0:
                    counter += 1
                if s[start] in count:
                    count[s[start]] += 1
                start += 1

        return best


print(Solution().minWindow("ADOBECODEBANC", 'ABC'))
print(Solution().minWindow("a", 'a'))
print(Solution().minWindow("a", 'aa'))
