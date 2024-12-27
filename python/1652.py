from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)

        if k == 0:
            return [0] * len(code)

        elif k > 0:
            k_sum = 0
            for i in range(0, k):
                k_sum += code[i % n]

            result = []
            for i in range(n):
                k_sum = k_sum - code[i] + code[(i + k) % n]
                result.append(k_sum)

            return result

        else:
            k = -k
            k_sum = 0
            for i in range(1, k + 1):
                k_sum += code[-i % n]

            result = [k_sum]
            for i in range(1, n):
                k_sum = k_sum + code[(i - 1) % n] - code[(i - k - 1) % n]
                result.append(k_sum)

            return result





# print(Solution().decrypt([5, 7, 1, 4], 3))
# print(Solution().decrypt([5, 7, 1, 4], 0))
print(Solution().decrypt([2,4,9,3], -2))


