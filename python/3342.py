import heapq
import math
from typing import List


class State:
    def __init__(self, x, y, distance, next_hop):
        self.x = x
        self.y = y
        self.distance = distance
        self.next_hop = next_hop

    def __lt__(self, other):
        if self.distance == other.distance:
            return self.next_hop < other.next_hop

        return self.distance < other.distance

class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        DIRECTIONS = [(0,1),(0,-1),(1,0),(-1,0)]
        n = len(moveTime)
        m = len(moveTime[0])

        distance = [[(math.inf, 1)] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]

        queue = [State(0, 0, 0, 1)]

        while queue:
            current = heapq.heappop(queue)

            if visited[current.x][current.y]:
                continue

            visited[current.x][current.y] = True

            new_next_hop = 2 if current.next_hop == 1 else 1
            for dx, dy in DIRECTIONS:
                new_x = current.x + dx
                new_y = current.y + dy

                if not (0 <= new_x < n and 0 <= new_y < m):
                    continue

                neighbor_distance = distance[new_x][new_y]
                candidate_distance = max(moveTime[new_x][new_y], current.distance) + current.next_hop

                if candidate_distance < neighbor_distance[0] or (candidate_distance == neighbor_distance[0] and new_next_hop < neighbor_distance[1]):
                    distance[new_x][new_y] = (candidate_distance, new_next_hop)
                    heapq.heappush(queue, State(new_x, new_y, candidate_distance, new_next_hop))

        return distance[n-1][m-1][0]

print(Solution().minTimeToReach([[0,4],[4,4]]))
print(Solution().minTimeToReach([[0,0,0,0],[0,0,0,0]]))
print(Solution().minTimeToReach([[0,1],[1,2]]))
