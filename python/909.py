import heapq
import math
from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        flatten_board = []

        reverse = False
        for r in range(n - 1, -1, -1):
            transverse = range(n - 1, -1, -1) if reverse else range(n)
            for c in transverse:
                flatten_board.append(-1 if board[r][c] == -1 else board[r][c] - 1)

            reverse = not reverse

        n2 = len(flatten_board)
        minimum = [float('inf')] * len(flatten_board)
        heap = [(0, 0)]
        while heap:
            (new_distance, i) = heapq.heappop(heap)
            if minimum[i] != -1 and new_distance >= minimum[i]:
                continue

            minimum[i] = new_distance

            for next_destination in range(i + 1, min(n2, i + 7)):
                if flatten_board[next_destination] != -1:
                    next_destination = flatten_board[next_destination]

                heapq.heappush(heap, (new_distance + 1, next_destination))

        return -1 if math.isinf(minimum[-1]) else minimum[-1]

print(Solution().snakesAndLadders([[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]))
print(Solution().snakesAndLadders([[-1,-1],[-1,3]]))
print(Solution().snakesAndLadders([[-1,-1,-1],[-1,9,8],[-1,8,9]]))
print(Solution().snakesAndLadders([[-1,-1,30,14,15,-1],[23,9,-1,-1,-1,9],[12,5,7,24,-1,30],[10,-1,-1,-1,25,17],[32,-1,28,-1,-1,32],[-1,-1,23,-1,13,19]]))
print(Solution().snakesAndLadders([[-1,-1,-1,-1,48,5,-1],[12,29,13,9,-1,2,32],[-1,-1,21,7,-1,12,49],[42,37,21,40,-1,22,12],[42,-1,2,-1,-1,-1,6],[39,-1,35,-1,-1,39,-1],[-1,36,-1,-1,-1,-1,5]]))