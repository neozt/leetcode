class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        top = 'ab'
        bot = 'ba'
        top_score = x
        bot_score = y
        if top_score < bot_score:
            top_score, bot_score = bot_score, top_score
            top, bot = bot, top

        stack = []
        result = 0

        for ch in s:
            if ch == top[1] and stack and stack[-1] == top[0]:
                stack.pop()
                result += top_score
            else:
                stack.append(ch)

        stack2 = []
        for ch in stack:
            if ch == bot[1] and stack2 and stack2[-1] == bot[0]:
                stack2.pop()
                result += bot_score
            else:
                stack2.append(ch)

        return result

# b  aabab
# b  aa  b
#

print(Solution().maximumGain("cdbcbbaaabab", 4, 5))
print(Solution().maximumGain("aabbaaxybbaabb", 5, 4))
