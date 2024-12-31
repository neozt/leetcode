from collections import Counter


class Solution:
    def maximumLength(self, s: str) -> int:
        best = -1
        for substring_length in range(1, len(s) + 1):
            counter = Counter()
            for i in range(0, len(s) - substring_length + 1):
                substring = s[i: i + substring_length]
                if is_special(substring):
                    counter[substring] += 1
                    if (counter[substring]) >= 3:
                        best = substring_length

        return best

def is_special(s: str) -> bool:
    return all(ch == s[0] for ch in s)


print(Solution().maximumLength("aaaa"))
print(Solution().maximumLength("abcdef"))
print(Solution().maximumLength("abcaba"))


