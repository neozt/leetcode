class Solution:
    def compressedString(self, word: str) -> str:
        prev_char = None
        count = 0

        result = []
        for ch in word:
            if prev_char is None or ch != prev_char or count == 9:
                if prev_char is not None:
                    result.append(str(count) + prev_char)
                prev_char = ch
                count = 1
            else:
                count += 1

        result.append(str(count) + prev_char)

        return ''.join(result)


print(Solution().compressedString("abcde"))
print(Solution().compressedString("aaaaaaaaaaaaaabb"))