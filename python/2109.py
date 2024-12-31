from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        index = 0
        index_with_spaces = 0
        i_spaces = 0
        result = ''
        while index < len(s):
            if i_spaces < len(spaces) and spaces[i_spaces] == index:
                result += ' '
                i_spaces += 1
                index_with_spaces += 1
            else:
                result += s[index]
                index += 1
                index_with_spaces += 1

        return result

print(Solution().addSpaces("LeetcodeHelpsMeLearn", [8,13,15]))
print(Solution().addSpaces("icodeinpython", [1,5,7,9]))
print(Solution().addSpaces("spacing", [0,1,2,3,4,5,6]))
