from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        unsatisfied = [customers[i] if grumpy[i] == 1 else 0 for i in range(len(customers))]
        print(unsatisfied)
        convertible = sum(unsatisfied[0:minutes])
        max_convertible = convertible
        for i in range(1, len(unsatisfied) - minutes + 1):
            convertible = convertible - unsatisfied[i - 1] + unsatisfied[i + minutes - 1]
            max_convertible = max(convertible, max_convertible)

        print(max_convertible)

        return sum(customers[i] for i in range(len(customers)) if grumpy[i] == 0) + max_convertible


# print(Solution().maxSatisfied([1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3))
# print(Solution().maxSatisfied([1], [0], 1))
print(Solution().maxSatisfied([3,2,5], [0,1,1], 2))

