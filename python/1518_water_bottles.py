class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        fullBottles = numBottles
        emptyBottles = 0

        result = 0
        while fullBottles > 0:
            result += fullBottles

            bottles = fullBottles + emptyBottles
            fullBottles = bottles // numExchange
            emptyBottles = bottles % numExchange

        return result


print(Solution().numWaterBottles(9, 3))
print(Solution().numWaterBottles(15, 4))
print(Solution().numWaterBottles(15, 8))
