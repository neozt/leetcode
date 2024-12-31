class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if n == 1:
            return 1

        return (self.findTheWinner(n - 1, k) + k) % n

print(Solution().findTheWinner(5, 2))
print(Solution().findTheWinner(6, 5))
