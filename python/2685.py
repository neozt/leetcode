from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, u: int):
        if self.parent[u] == u:
            return u

        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u: int, v: int):
        parent_u = self.find(u)
        parent_v = self.find(v)

        if parent_u == parent_v:
            return

        if parent_v > parent_u:
            self.parent[parent_u] = parent_v
            self.rank[parent_v] += self.rank[parent_u]
        else :
            self.parent[parent_v] = parent_u
            self.rank[parent_u] += self.rank[parent_v]

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        uf = UnionFind(n)

        # Form connected components
        for u, v in edges:
            uf.union(u, v)
        components = defaultdict(list)
        for i in range(n):
            components[uf.find(i)].append(i)

        # Count how many vertices there are in a component
        edge_count = defaultdict(int)
        for u, v in edges:
            edge_count[uf.find(u)] += 1

        # A component is complete if and only if there are m(m-1)/2 edges between the vertexes
        # Eg, for a component with m = 1 vertices, we need 0 edges for it to be complete
        # for m = 2, 0 + 1 edges required
        # for m = 3, 0 + 1 + 2 edges required
        # for m = 4, 0 + 1 + 2 + 3 edges required
        # Therefore, we can use arithmetic sequence formula to calculate the edges required given m vertices.
        result = 0
        for i in range(n):
            if i != uf.find(i):
                # We are looping through component, so we only look at the representatives
                continue

            m = uf.rank[i]
            if (m * (m - 1) // 2) == edge_count[i]:
                result += 1

        return result

print(Solution().countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4]]))
print(Solution().countCompleteComponents(6, [[0,1],[0,2],[1,2],[3,4],[3,5]]))
