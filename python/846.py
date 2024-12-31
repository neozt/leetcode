from collections import defaultdict
from typing import List


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        char_count = defaultdict(int)

        for h in hand:
            char_count[h] += 1

        for n in sorted(char_count.keys()):
            while char_count[n] > 0:
                for i in range(groupSize):
                    if char_count[n + i] <= 0:
                        return False
                    char_count[n + i] -= 1

        return True


print(Solution().isNStraightHand([1, 2, 3, 6, 2, 3, 4, 7, 8], 3))
print(Solution().isNStraightHand([1,2,3,4,5], 4))
