class Solution:
    def compressedString(self, word: str) -> str:
        chars = []
        count = []

        for ch in word:
            if not chars or ch != chars[-1] or count[-1] == 9:
                chars.append(ch)
                count.append(1)
            else:
                count[-1] += 1

        return ''.join((str(count) + ch) for ch, count in zip(chars, count))


print(Solution().compressedString("abcde"))
print(Solution().compressedString("aaaaaaaaaaaaaabb"))