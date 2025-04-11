class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for num in range(low, high + 1):
            num_str = str(num)
            if len(num_str) % 2 != 0:
                continue

            first_half_sum = sum(int(digit) for digit in num_str[:len(num_str) // 2])
            second_half_sum = sum(int(digit) for digit in num_str[len(num_str) // 2:])

            if first_half_sum == second_half_sum:
                result += 1

        return result

print(Solution().countSymmetricIntegers(1, 100))
print(Solution().countSymmetricIntegers(1200, 1230))

