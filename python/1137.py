class Solution:
    def tribonacci(self, n: int) -> int:
        # T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0
        if (n == 0):
            return 0
        if (n == 1 or n == 2):
            return 1

        prevPrev = 0
        prev = 1
        current = 1

        for i in range(3, n+1):
            prevPrev, prev, current =  prev, current, current + prev + prevPrev

        return current


print(Solution().tribonacci(0))
print(Solution().tribonacci(1))
print(Solution().tribonacci(2))
print(Solution().tribonacci(4))
print(Solution().tribonacci(25))
