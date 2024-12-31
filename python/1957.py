class Solution:
    def makeFancyString(self, s: str) -> str:
        result = ""
        previous_char = None
        occurence = 0
        for i in range(len(s)):
            char = s[i]
            if char == previous_char:
                occurence += 1
                if occurence < 3:
                    result += char
            else:
                previous_char = char
                occurence = 1
                result += char
        return result

print(Solution().makeFancyString('leeetcode'))
print(Solution().makeFancyString('aaabaaaa'))
print(Solution().makeFancyString('aab'))
