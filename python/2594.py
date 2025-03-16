import math
from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def can_repair_in_minutes(minutes: int) -> bool:
            cars_repaired = 0
            for rank in ranks:
                cars_repaired += math.floor(math.sqrt(minutes / rank))
                if cars_repaired >= cars:
                    return True

            return False

        min_rank = min(ranks)

        left = 0
        right = min_rank * cars * cars

        while left < right:
            mid = (left + right) // 2
            if can_repair_in_minutes(mid):
                right = mid
            else:
                left = mid + 1

        return left


print(Solution().repairCars([4,2,3,1], 10))
print(Solution().repairCars([5,1,8], 6))
