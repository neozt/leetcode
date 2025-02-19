from typing import List


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.answer = ''
        self.strings_generated = 0
        def backtrack(current: List[str]) -> None:
            if len(current) == n:
                self.strings_generated += 1
                if self.strings_generated == k:
                    self.answer = ''.join(current)
                return

            for ch in ['a', 'b', 'c']:
                if current and current[-1] == ch:
                    continue

                current.append(ch)
                backtrack(current)
                current.pop()

                if self.answer:
                    # Already found the answer, can return early
                    return


        backtrack([])

        return self.answer

print(Solution().getHappyString(1, 3))
print(Solution().getHappyString(1, 4))
print(Solution().getHappyString(3, 9))
