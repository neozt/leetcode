from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        left = 0
        while left <= len(arr) - 3:
            right = left
            while arr[right] % 2 == 1:
                right += 1
                if right - left == 3:
                    return True

            left = right + 1

        return False


print(Solution().threeConsecutiveOdds([2, 6, 4, 1]))
print(Solution().threeConsecutiveOdds([1, 2, 34, 3, 4, 5, 7, 23, 12]))
print(Solution().threeConsecutiveOdds([1, 1, 1]))
