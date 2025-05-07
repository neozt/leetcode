import heapq
from typing import List

class State:
    def __init__(self, x, y, distance):
        self.x = x
        self.y = y
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]

        inf = float('inf')
        distances = [[inf] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]

        queue = []
        heapq.heappush(queue, State(0,0,0))

        while queue:
            current = heapq.heappop(queue)
            if visited[current.x][current.y]:
                continue

            visited[current.x][current.y] = True

            for dx, dy in DIRECTIONS:
                new_x, new_y = current.x + dx, current.y + dy

                if not (0 <= new_x < n and 0 <= new_y < m):
                    continue

                new_distance = max(current.distance, moveTime[new_x][new_y]) + 1

                if new_distance < distances[new_x][new_y]:
                    distances[new_x][new_y] = new_distance
                    heapq.heappush(queue, State(new_x, new_y, new_distance))

        return distances[n - 1][m - 1]

print(Solution().minTimeToReach([[0,4],[4,4]]))
print(Solution().minTimeToReach([[0,0,0],[0,0,0]]))
print(Solution().minTimeToReach([[0,1],[1,2]]))
