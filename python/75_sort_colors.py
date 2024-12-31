from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0, 0, 0]

        for n in nums:
            count[n] += 1

        i = 0
        for n, cnt in enumerate(count):
            for j in range(cnt):
                nums[i] = n
                i += 1


a = [2,0,2,1,1,0]
Solution().sortColors(a)
print(a)

b = [2,0,1]
Solution().sortColors(b)
print(b)