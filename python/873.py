from typing import List


class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        result = 0

        dp = [[0] * len(arr) for _ in range(len(arr))]

        val_to_index = {num: index for index, num in enumerate(arr)}

        for right in range(1, len(arr)):
            for left in range(0, right):
                diff = arr[right] - arr[left]
                previous_index = val_to_index.get(diff, -1)

                dp[left][right] = (
                    dp[previous_index][left] + 1
                    if diff < arr[left] and previous_index >= 0
                    else 2
                )
                result = max(result, dp[left][right])

        return result if result > 2 else 0


print(Solution().lenLongestFibSubseq([1,2,3,4,5,6,7,8]))
print(Solution().lenLongestFibSubseq([1,3,7,11,12,14,18]))
