from collections import Counter, deque
from typing import List, Deque


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        count = Counter(digits)
        result = set()

        def backtrack(path: Deque[int], remaining: Counter[int]):
            nonlocal result

            if len(path) == 3:
                result.add(''.join(str(d) for d in path))
                return

            for digit, freq in remaining.items():
                if freq == 0:
                    continue

                if len(path) == 0 and digit not in [0,2,4,6,8]:
                    continue

                if len(path) == 2 and digit == 0:
                    continue

                path.appendleft(digit)
                remaining[digit] -= 1
                backtrack(path, remaining)
                path.popleft()
                remaining[digit] += 1

        backtrack(deque(), count)

        return list(sorted(int(r) for r in result))


print(Solution().findEvenNumbers([2,1,3,0]))
print(Solution().findEvenNumbers([2,2,8,8,2]))
print(Solution().findEvenNumbers([3,7,5]))
