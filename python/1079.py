from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)
        sequences = set()

        populate_sequences('', sequences, counter)

        return len(sequences)

def populate_sequences(current: str, sequences, counter) -> None:
    for ch, count in counter.items():
        if not count:
            continue

        sequences.add(current + ch)

        counter[ch] -= 1
        populate_sequences(current + ch, sequences, counter)
        counter[ch] += 1


print(Solution().numTilePossibilities('AAB'))
print(Solution().numTilePossibilities('AAABBC'))
print(Solution().numTilePossibilities('V'))
