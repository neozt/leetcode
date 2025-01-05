from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        diff_array = [0] * len(s)

        for shift in shifts:
            start, end, direction = shift
            shift_by = 1 if direction == 1 else -1
            diff_array[start] += shift_by
            if end + 1 < len(s):
                diff_array[end + 1] -= shift_by

        result = []
        shift_by = 0
        for i in range(len(s)):
            shift_by += diff_array[i]
            result += shift_letter(s[i], shift_by)

        return ''.join(result)


def shift_letter(letter: str, shift_by: int):
    return chr(((ord(letter) - ord('a') + shift_by) % 26) + ord('a'))


print(Solution().shiftingLetters('abc', [[0,1,0],[1,2,1],[0,2,1]]))
print(Solution().shiftingLetters('dztz', [[0,0,0],[1,1,1]]))
