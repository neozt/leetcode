from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        numbers = set()

        for num in nums:
            numbers.add(int(num, 2))

        for i in range(2 ** len(nums)):
            if i not in numbers:
                return bin(i)[2:].zfill(len(nums))

        raise Exception()

print(Solution().findDifferentBinaryString(["01","10"]))
print(Solution().findDifferentBinaryString(["00","01"]))
print(Solution().findDifferentBinaryString(["111","011","001"]))
