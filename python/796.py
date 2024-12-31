class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        return any(self.isEqualWithOffset(s, goal, i) for i in range(len(s)))

    def isEqualWithOffset(self, s, goal, offset):
        for j in range(len(s)):
            if s[(j+offset) % len(s)] != goal[j]:
                return False
        return True

print(Solution().rotateString("abcde", "cdeab"))
print(Solution().rotateString("abcde", "abced"))
# print(Solution().rotateString())
# print(Solution().rotateString())
