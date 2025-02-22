# Definition for a binary tree node.
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        nodes = deque()
        depth = 0
        value = ''
        for i, ch in enumerate(traversal):
            if ch == '-':
                if i > 0 and traversal[i - 1] != '-':
                    nodes.append((int(value), depth))
                    depth = 1
                    value = ''
                else:
                    depth += 1
            else:
                value += ch

        if value:
            nodes.append((int(value), depth))

        return self.dfs(nodes, 0)

    def dfs(self, nodes, current_depth):
        if not nodes:
            return None

        _, depth = nodes[0]

        if depth != current_depth:
            return None

        value, _ = nodes.popleft()
        return TreeNode(
            value,
            self.dfs(nodes, current_depth + 1),
            self.dfs(nodes, current_depth + 1)
        )


print(Solution().recoverFromPreorder("1-2--3--4-5--6--7"))


