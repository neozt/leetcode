from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_to_max = [-1] * 82
        best = -1
        for num in nums:
            digits_sum = calculate_digits_sum(num)
            if sum_to_max[digits_sum] != -1:
                best = max(best, sum_to_max[digits_sum] + num)
            sum_to_max[digits_sum] = max(sum_to_max[digits_sum], num)

        return best


def calculate_digits_sum(num: int) -> int:
    result = 0
    while num:
        div, mod = divmod(num ,10)
        result += mod
        num = div

    return result


print(Solution().maximumSum([18,43,36,13,7]))
print(Solution().maximumSum([10,12,19,14]))
