from typing import List


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n + 1)]

    def find(self, n):
        while self.parent[n] != self.parent[self.parent[n]]:
            self.parent[n] = self.parent[self.parent[n]]
        return self.parent[n]

    def union(self, n1, n2):
        self.parent[self.find(n1)] = self.find(n2)

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges))
        for edge in edges:
            n1, n2 = edge
            if uf.find(n1) == uf.find(n2):
                return edge
            uf.union(n1, n2)

        raise Exception

print(Solution().findRedundantConnection([[1,2],[1,3],[2,3]]))
print(Solution().findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))
