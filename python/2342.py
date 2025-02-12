from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        sum_to_max = {}
        best = -1
        for num in nums:
            digits_sum = calculate_digits_sum(num)
            if digits_sum in sum_to_max:
                best = max(best, sum_to_max[digits_sum] + num)

            sum_to_max[digits_sum] = max(sum_to_max.get(digits_sum, 0), num)

        return best


def calculate_digits_sum(num: int) -> int:
    result = 0
    while num:
        result += num % 10
        num = num // 10

    return result


print(Solution().maximumSum([18,43,36,13,7]))
print(Solution().maximumSum([10,12,19,14]))
