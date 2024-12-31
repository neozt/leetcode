from typing import List


class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []
        for i in range(len(prices)):
            best = None
            for j in range(i+1, len(prices)):
                if prices[j] <= prices[i]:
                    best = prices[j]
                    break
            discount = best if best is not None else 0
            answer.append(prices[i] - discount)

        return answer
