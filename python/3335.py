class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        MOD = 10 ** 9 + 7
        count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for _ in range(t):
            original_z_count = count[25]
            for i in range(25, 0, -1):
                count[i] = count[(i - 1 + 26) % 26]

            count[1] = (count[0] + original_z_count) % MOD
            count[0] = original_z_count

        total = 0
        for cnt in count:
            total = (total + cnt) % MOD

        return total

print(Solution().lengthAfterTransformations("abcyy", 2))
print(Solution().lengthAfterTransformations("azbk", 1))
