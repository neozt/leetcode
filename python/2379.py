class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count_w = sum(b == 'W' for b in blocks[0:k])
        best = count_w
        for i in range(1, len(blocks) - k + 1):
            if blocks[i - 1] == 'W':
                count_w -= 1
            if blocks[i + k - 1] == 'W':
                count_w += 1
            best = min(best, count_w)

        return best


print(Solution().minimumRecolors("WBBWWBBWBW", 7))
print(Solution().minimumRecolors("WBWBBBW", 2))
print(Solution().minimumRecolors("WWBBBWBBBBBWWBWWWB", 16))
