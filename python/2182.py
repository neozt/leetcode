import heapq
from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        heap = [(-ord(ch), ch, f) for (ch, f) in freq.items()]
        heapq.heapify(heap)

        result = ''

        while heap:
            _, largest_char, f = heapq.heappop(heap)
            consecutive = 0
            while f > 0:
                if consecutive < repeatLimit:
                    consecutive += 1
                    result += largest_char
                    f -= 1
                else:
                    if not heap:
                        break
                    else:
                        priority, next_largest_char, next_largest_f = heapq.heappop(heap)
                        result += next_largest_char
                        consecutive = 0
                        if next_largest_f > 1:
                            heapq.heappush(heap, (priority, next_largest_char, next_largest_f - 1))

        return result

print(Solution().repeatLimitedString("cczazcc", 3))
print(Solution().repeatLimitedString("aababab", 2))

