class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        # Find first occurence of ch in word
        i = 0
        while i < len(word):
            if word[i] == ch:
                break
            i += 1
        if i >= len(word):
            return word

        # Reverse prefix and append suffix
        return word[i::-1] + word[i+1:]


print(Solution().reversePrefix("abcdefd", 'd'))
print(Solution().reversePrefix("xyxzxe", 'z'))
print(Solution().reversePrefix("abcd", 'z'))
