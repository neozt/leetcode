class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        words = sentence.split(' ')
        for i in range(len(words)):
            word = words[i]
            prev_word = words[(i-1) % len(words)]
            if word[0] != prev_word[-1]:
                return False
        return True

print(Solution().isCircularSentence("leetcode exercises sound delightful"))
print(Solution().isCircularSentence("eetcode"))
print(Solution().isCircularSentence("Leetcode is cool"))
