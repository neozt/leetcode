class Solution:
    def minimumLength(self, s: str) -> int:
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        return sum(reduce(n) for n in count)

def reduce(n: int) -> int:
    if n == 0:
        return 0

    if n % 2 == 0:
        return 2

    return 1