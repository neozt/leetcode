from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        result = []

        for i, num in enumerate(nums):
            result.append('1' if num[i] == '0' else '0')

        return ''.join(result)

print(Solution().findDifferentBinaryString(["01","10"]))
print(Solution().findDifferentBinaryString(["00","01"]))
print(Solution().findDifferentBinaryString(["111","011","001"]))
