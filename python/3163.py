class Solution:
    def compressedString(self, word: str) -> str:
        prev_char = word[0]
        count = 1

        result = []
        for ch in word[1:]:
            if ch != prev_char or count == 9:
                result.append(str(count) + prev_char)
                prev_char = ch
                count = 1
            else:
                count += 1

        result.append(str(count) + prev_char)

        return ''.join(result)


print(Solution().compressedString("abcde"))
print(Solution().compressedString("aaaaaaaaaaaaaabb"))