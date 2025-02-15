from functools import cache


class Solution:
    def punishmentNumber(self, n: int) -> int:
        result = 0
        for i in range(1, n + 1):
            if is_partitionable_square(i):
                result += i * i

        return result

def is_partitionable_square(i: int) -> bool:
    squared = i * i
    return helper(str(squared), 0, 0, 0, i)

@cache
def helper(digits: str, start_index: int, stop_index: int, current_sum: int, target_sum: int) -> bool:
    if stop_index > len(digits):
        return False
    if start_index >= len(digits):
        return target_sum == current_sum
    if current_sum > target_sum:
        return False


    return (helper(digits, stop_index + 1, stop_index + 1, current_sum + int(digits[start_index:stop_index + 1]),target_sum)
            or helper(digits, start_index, stop_index + 1, current_sum, target_sum))



print(Solution().punishmentNumber(10))
print(Solution().punishmentNumber(37))
