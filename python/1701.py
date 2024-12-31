from typing import List


class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        current_time = 1
        total_wait = 0
        for [arrival, time] in customers:
            current_time = max(current_time, arrival) + time
            total_wait += max(0, current_time - arrival)

        return total_wait / len(customers)


print(Solution().averageWaitingTime([[1, 2], [2, 5], [4, 3]]))
print(Solution().averageWaitingTime([[5,2],[5,4],[10,3],[20,1]]))
