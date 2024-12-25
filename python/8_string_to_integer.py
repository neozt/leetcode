class Solution:
    def myAtoi(self, s: str) -> int:
        start = 0
        while start < len(s) and s[start] == ' ':
            start += 1

        is_positive = True
        if start < len(s) and s[start] in '-+':
            is_positive = s[start] == '+'
            start += 1

        digits = '0123456789'
        acc = 0
        MAX_POSITIVE = pow(2, 31) - 1
        MAX_NEGATIVE = pow(2, 31)
        while start < len(s) and s[start] in digits:
            next_digit = int(s[start])
            if is_positive:
                if (MAX_POSITIVE - next_digit) / 10 < acc:
                    return MAX_POSITIVE
            elif not is_positive:
                if (MAX_NEGATIVE - next_digit) / 10 < acc:
                    return -MAX_NEGATIVE

            acc = 10 * acc + next_digit
            start += 1

        return acc * (1 if is_positive else -1)


print(Solution().myAtoi("42"))
print(Solution().myAtoi("   -42"))
print(Solution().myAtoi("4193 with words"))
