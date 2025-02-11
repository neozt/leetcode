class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        result = ''

        for ch in s:
            result += ch
            if len(result) >= len(part) and result[-len(part):] == part:
                result = result[:-len(part)]

        return result


print(Solution().removeOccurrences("daabcbaabcbc", 'abc'))
print(Solution().removeOccurrences("axxxxyyyyb", 'xy'))
