from typing import List


class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        result = [-1] * ((n - 1) * 2 + 1)
        candidates = [i for i in range(n, 0, -1)] # Greedy algorithm: Should always try to fill with the largest candidate first

        def backtrack(index: int) -> bool:
            if index == len(result):
                return True

            if result[index] != -1:
                # Already filled, go next
                return backtrack(index + 1)

            # Try to fill with a candidate and check recursively if it will be valid
            for candidate_index, candidate in enumerate(candidates):
                if (
                        candidate == 1
                        or (index + candidate < len(result) and result[index + candidate] == -1) # Check if can fill with candidate
                ):
                    result[index] = candidate
                    if candidate != 1:
                        result[index + candidate] = candidate
                    candidates.pop(candidate_index)

                    if backtrack(index + 1):
                        return True

                    # Undo changes
                    result[index] = -1
                    if candidate != 1:
                        result[index + candidate] = -1
                    candidates.insert(candidate_index, candidate)

            return False

        backtrack(0)

        return result

print(Solution().constructDistancedSequence(3))
print(Solution().constructDistancedSequence(5))

