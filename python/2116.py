class Solution:
    ANY = 'A'
    OPEN = '('
    CLOSE = ')'

    UNLOCKED = '0'
    LOCKED = '1'

    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        open_brackets = []
        unlocked_brackets = []
        for i in range(len(s)):
            if locked[i] == self.UNLOCKED:
                unlocked_brackets.append(i)
            elif s[i] == self.OPEN:
                open_brackets.append(i)
            else:
                # Always try to match with open brackets before unlocked brackets
                if open_brackets:
                    open_brackets.pop()
                elif unlocked_brackets:
                    unlocked_brackets.pop()
                else:
                    # Unmatched close bracket, return false
                    return False

        while open_brackets and unlocked_brackets:
            if open_brackets[-1] > unlocked_brackets[-1]:
                # Unmatched open bracket, return false
                return False

            open_brackets.pop()
            unlocked_brackets.pop()

        if open_brackets:
            # Unmatched open bracket, return false
            return False

        return True


print(Solution().canBeValid("))()))", "010100"))
print(Solution().canBeValid("()()", "0000"))
print(Solution().canBeValid(")", "0"))
print(Solution().canBeValid("())()))()(()(((())(()()))))((((()())(())", "1011101100010001001011000000110010100101"))
