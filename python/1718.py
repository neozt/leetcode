from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [-1] * ((n - 1) * 2 + 1)
        candidates = [i for i in range(n, 0, -1)]

        backtrack(result, candidates, 0, n)

        return result

def backtrack(result: List[int], candidates: List[int], index: int, n: int) -> bool:
    if index == len(result):
        return True

    if result[index] != -1:
        # Already filled, go next
        return backtrack(result, candidates, index + 1, n)

    for candidate in candidates:
        if candidate == 1:
            result[index] = candidate
            if backtrack(result, list(filter(lambda x : x != candidate, candidates)), index + 1, n):
                return True
            result[index] = -1
        else:
            if index + candidate < len(result) and result[index + candidate] == -1:
                result[index + candidate] = result[index] = candidate
                if backtrack(result, list(filter(lambda x : x != candidate, candidates)), index + 1, n):
                    return True
                result[index + candidate] = result[index] = -1

    return False

print(Solution().constructDistancedSequence(3))
print(Solution().constructDistancedSequence(5))

