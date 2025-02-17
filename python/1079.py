from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)

        result = set()

        def backtrack(current: str) -> None:
            for ch, count in counter.items():
                if not count:
                    continue

                result.add(current + ch)

                counter[ch] -= 1
                backtrack(current + ch)
                counter[ch] += 1

        backtrack('')

        return len(result)


print(Solution().numTilePossibilities('AAB'))
print(Solution().numTilePossibilities('AAABBC'))
print(Solution().numTilePossibilities('V'))
