from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s) - 1
        while end > start:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        print(s)


print(Solution().reverseString(["h","e","l","l","o"]))
print(Solution().reverseString(["h","e","l","o"]))
