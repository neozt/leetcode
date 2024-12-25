from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digit_map = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        result = []

        def backtrack(i, temp):
            if i == len(digits):
                result.append("".join(temp))
                return

            for ch in digit_map[digits[i]]:
                temp.append(ch)
                backtrack(i + 1, temp)
                temp.pop()

        backtrack(0, [])

        return result



print(Solution().letterCombinations("23"))
print(Solution().letterCombinations(""))
print(Solution().letterCombinations("5"))

