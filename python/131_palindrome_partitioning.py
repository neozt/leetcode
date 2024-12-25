from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]

        valid_paths = []
        def backtrack(start, path):
            if start == len(s):
                valid_paths.append(path.copy())
                return

            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path)
                    path.pop()

        backtrack(0, [])

        return valid_paths

print(Solution().partition('aab'))
print(Solution().partition('a'))
