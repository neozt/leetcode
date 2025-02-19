from typing import List


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        def backtrack(current: List[str]) -> None:
            if len(current) == n:
                result.append(''.join(current))
                return

            for ch in ['a', 'b', 'c']:
                if current and current[-1] == ch:
                    continue

                current.append(ch)
                backtrack(current)
                current.pop()

        backtrack([])
        if k > len(result):
            return ''

        return result[k-1]

print(Solution().getHappyString(1, 3))
print(Solution().getHappyString(1, 4))
print(Solution().getHappyString(3, 9))
