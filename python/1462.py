from functools import cache
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)] # graph of course pointing to its prerequisites
        for prerequisite, course in prerequisites:
            graph[course].append(prerequisite)

        @cache
        def find_prerequisites_recursive(course):
            result = set()
            for prereq in graph[course]:
                result.add(prereq)
                result.update(find_prerequisites_recursive(prereq))

            return result

        return [candidate in find_prerequisites_recursive(course) for candidate, course in queries]

print(Solution().checkIfPrerequisite(2, [[1,0]], [[0,1],[1,0]]))
print(Solution().checkIfPrerequisite(2, [], [[1,0],[0,1]]))
print(Solution().checkIfPrerequisite(3, [[1,2],[1,0],[2,0]], [[1,0],[1,2]]))
