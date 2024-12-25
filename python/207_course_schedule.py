from typing import List, Set


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {}
        for (course, prereq) in prerequisites:
            if (course not in prereqs):
                prereqs[course] = []
            prereqs[course].append(prereq)

        memo = {}
        for course in range(numCourses):
            result = self.dfs(course, prereqs, memo)
            if (not result):
                return False

        return True

    def dfs(self, current: int, graph: dict[int, List[int]], memo: dict[int, bool]):
        if current in memo:
            return memo[current]

        if not graph.get(current):
            return True

        memo[current] = False # Temporarily set to false so that if any prerequisite has current as a prerequisite, it will return False, thus detecting a cycle
        memo[current] = all(self.dfs(prereq, graph, memo) for prereq in graph[current])
        return memo[current]


print(Solution().canFinish(2, [[1,0]]))
print(Solution().canFinish(2, [[1,0], [0,1]]))
