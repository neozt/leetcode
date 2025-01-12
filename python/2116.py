class Solution:
    ANY = 'A'
    OPEN = '('
    CLOSE = ')'

    UNLOCKED = '0'
    LOCKED = '1'

    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 != 0:
            return False

        combined = ['A' if l == '0' else p for p, l in zip(s, locked)]

        open_count = 0
        any_count = 0
        # First pass from left to check that all close parenthesis can be matched
        for p in combined:
            if p == self.CLOSE:
                if not open_count and not any_count:
                    # Unmatched close parenthesis
                    return False

                if open_count: # Try match with locked open parenthesis first
                    open_count -= 1
                else: # Then only flexible parenthesis
                    any_count -= 1
            elif p == self.OPEN:
                open_count += 1
            else:
                any_count += 1

        close_count = 0
        any_count = 0
        # Second pass from right to check that all close parenthesis can be matched
        for p in reversed(combined):
            if p == self.OPEN:
                if not close_count and not any_count:
                    # Unmatched open parenthesis
                    return False

                if close_count: # Try match with locked close parenthesis first
                    close_count -= 1
                else: # Then only flexible parenthesis
                    any_count -= 1
            elif p == self.CLOSE:
                close_count += 1
            else:
                any_count += 1

        return True


print(Solution().canBeValid("))()))", "010100"))
print(Solution().canBeValid("()()", "0000"))
print(Solution().canBeValid(")", "0"))
print(Solution().canBeValid("())()))()(()(((())(()()))))((((()())(())", "1011101100010001001011000000110010100101"))
