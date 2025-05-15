from typing import List

# TODO TLE
class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        MOD = 10 ** 9 + 7

        count = [0] * 26
        new_count = [0] * 26
        for ch in s:
            count[ord(ch) - ord('a')] += 1

        for _ in range(t):
            for i in range(26):
                new_count[i] = 0

            for i in range(26):
                for j in range(nums[i]):
                    new_count[(i + j + 1) % 26] = (new_count[(i + j + 1) % 26] + count[i]) % MOD

            count, new_count = new_count, count


        result = 0
        for cnt in count:
            result = (result + cnt) % MOD
        return result


print(Solution().lengthAfterTransformations("abcyy", 2, [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2]))
print(Solution().lengthAfterTransformations("azbk", 1, [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]))
