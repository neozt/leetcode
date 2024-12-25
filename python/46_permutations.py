from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        self.result = []
        self.used = [False] * len(nums)
        self.path = []
        self.backtrack(nums)
        return self.result

    def backtrack(self, nums: List[int]):
        if len(self.path) == len(nums):
            self.result.append(self.path.copy())
            return

        for i in range(len(nums)):
            if not self.used[i]:
                self.used[i] = True
                self.path.append(nums[i])
                self.backtrack(nums)
                self.used[i] = False
                self.path.pop()


print(Solution().permute([1, 2, 3]))
print(Solution().permute([0,1]))
print(Solution().permute([1]))
