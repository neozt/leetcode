from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        difficulty_profit = sorted(zip(difficulty, profit), key=lambda x: x[0])
        worker = sorted(worker)

        best_profit = 0
        i = 0
        result = 0
        for w in worker:
            while i < len(difficulty_profit) and difficulty_profit[i][0] <= w:
                best_profit = max(best_profit, difficulty_profit[i][1])
                i += 1

            result += best_profit

        return result


print(Solution().maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7]))
print(Solution().maxProfitAssignment([85,47,57], [24,66,99], [40,25,25]))

