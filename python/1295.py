from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            if hasEvenDigitCount(num):
                result += 1

        return result


def hasEvenDigitCount(num):
    isEven = True
    while num:
        isEven = not isEven
        num = num // 10

    return isEven
