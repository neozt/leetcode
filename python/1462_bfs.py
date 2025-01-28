from collections import deque
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)] # graph of course pointing to its prerequisites
        for prerequisite, course in prerequisites:
            graph[course].append(prerequisite)

        is_prerequisite = [[False] * numCourses for _ in range(numCourses)]
        # Do BFS to find all prerequisites for each course
        for course in range(numCourses):
            q = deque([course])
            while q:
                c = q.popleft()
                if is_prerequisite[course][c]:
                    continue

                is_prerequisite[course][c] = True
                for n in graph[c]:
                    q.append(n)

        return [is_prerequisite[course][candidate] for candidate, course in queries]

print(Solution().checkIfPrerequisite(2, [[1,0]], [[0,1],[1,0]]))
print(Solution().checkIfPrerequisite(2, [], [[1,0],[0,1]]))
print(Solution().checkIfPrerequisite(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]))
