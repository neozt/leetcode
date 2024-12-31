class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        i = 0
        j = 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j] or is_cyclic_increment(str1[i], str2[j]):
                i += 1
                j += 1
            else:
                i += 1

        return j == len(str2)

def is_cyclic_increment(a: str, b: str) -> bool:
    if a == 'z' and b == 'a':
        return True

    return ord(b) - ord(a) == 1


print(Solution().canMakeSubsequence('abc', 'ad'))
print(Solution().canMakeSubsequence('zc', 'ad'))
print(Solution().canMakeSubsequence('ab', 'd'))
