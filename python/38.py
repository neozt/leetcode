class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'

        return self.compress(self.countAndSay(n - 1))

    def compress(self, s: str) -> str:
        result = ''
        prev_char: None | str = None
        prev_count: None | int = None
        for ch in s:
            if ch != prev_char:
                if prev_char:
                    result += str(prev_count) + prev_char
                prev_char = ch
                prev_count = 1
            else:
                prev_count += 1
        if prev_char:
            result += str(prev_count) + prev_char

        return result

print(Solution().countAndSay(4))
print(Solution().countAndSay(1))
