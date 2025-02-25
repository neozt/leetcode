from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10 ** 9 + 7

        result = 0
        dp_odd = 0
        dp_even = 0
        for num in arr:
            is_even = num % 2 == 0
            if is_even:
                dp_odd, dp_even = dp_odd, (dp_even + 1) % MOD
            else:
                dp_odd, dp_even = (dp_even + 1) % MOD, dp_odd

            result = (result + dp_odd) % MOD

        return result

print(Solution().numOfSubarrays([1,3,5]))
print(Solution().numOfSubarrays([2,4,6]))
print(Solution().numOfSubarrays([1,2,3,4,5,6,7]))

