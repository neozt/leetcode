from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        low = 1
        high = max(bloomDay)

        while low < high:
            middle = (high + low) // 2
            if self.can_make_bouquet(middle, bloomDay, m, k):
                high = middle
            else:
                low = middle + 1

        return low

    def can_make_bouquet(self, currentDay, bloomDay, m, k):
        i = 0
        j = 0
        bouquets = 0
        while j < len(bloomDay):
            if currentDay >= bloomDay[j]:
                if j - i + 1 >= k:
                    bouquets += 1
                    if bouquets == m:
                        return True

                    i = j + 1
                    j = j + 1
                else:
                    j += 1

            else:
                i = j + 1
                j = j + 1

        return False

print(Solution().minDays([1, 10, 3, 10, 2], 3, 1))
print(Solution().minDays([1,10,3,10,2], 3, 2))
print(Solution().minDays([7,7,7,7,12,7,7], 2, 3))
