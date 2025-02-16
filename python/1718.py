from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [-1] * ((n - 1) * 2 + 1)
        candidates = [i for i in range(n, 0, -1)]

        def backtrack(index: int) -> bool:
            if index == len(result):
                return True

            if result[index] != -1:
                # Already filled, go next
                return backtrack(index + 1)

            for candidate in candidates:
                if candidate == 1:
                    result[index] = candidate
                    position = candidates.index(candidate)
                    candidates.pop(position)
                    if backtrack(index + 1):
                        return True
                    # backtrack
                    result[index] = -1
                    candidates.insert(position, candidate)
                else:
                    if index + candidate < len(result) and result[index + candidate] == -1:
                        result[index + candidate] = result[index] = candidate
                        position = candidates.index(candidate)
                        candidates.pop(position)
                        if backtrack(index + 1):
                            return True
                        result[index + candidate] = result[index] = -1
                        candidates.insert(position, candidate)

            return False

        backtrack(0)

        return result

print(Solution().constructDistancedSequence(3))
print(Solution().constructDistancedSequence(5))

