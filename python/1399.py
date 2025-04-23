from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        counts = defaultdict(int)
        for num in range(1, n + 1):
            current_sum = self.sum_digits(num)
            counts[current_sum] += 1

        largest_size = 0
        count = 0
        for size in counts.values():
            if size > largest_size:
                largest_size = size
                count = 1
            elif size == largest_size:
                count += 1

        return count

    def sum_digits(self, n: int) -> int:
        result = 0
        while n:
            result += n % 10
            n = n // 10

        return result

print(Solution().countLargestGroup(13))