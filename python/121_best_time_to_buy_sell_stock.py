from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = float('inf')
        best = 0
        for price in prices:
            profit = price - lowest_price
            if profit > best:
                best = profit

            if price < lowest_price:
                lowest_price = price

        return best