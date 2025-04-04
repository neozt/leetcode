from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'TreeNode({self.val})'


class Solution:
    def __init__(self):
        self.max_depth = -1
        self.lca: list[TreeNode] = []

    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def dfs(node: Optional[TreeNode], path: list[TreeNode], current_depth: int):
            if not node:
                return

            path.append(node)
            if not node.left and not node.right:
                if current_depth > self.max_depth:
                    self.max_depth = current_depth
                    self.lca = path.copy()
                elif current_depth == self.max_depth:
                    lca = []
                    for i in range(len(self.lca)):
                        if self.lca[i] != path[i]:
                            break
                        lca.append(path[i])
                    self.lca = lca

            else:
                dfs(node.left, path, current_depth + 1)
                dfs(node.right, path, current_depth + 1)

            path.pop()

        dfs(root, [], 0)
        return self.lca[-1]

# print(Solution().lcaDeepestLeaves(TreeNode(1)))


n7 = TreeNode(7)
n4 = TreeNode(4)
n2 = TreeNode(2, n7, n4)
n6 = TreeNode(6)
n5 = TreeNode(5, n6, n2)
n0 = TreeNode(0)
n8 = TreeNode(8)
n1 = TreeNode(1, n0, n8)
n3 = TreeNode(3, n5, n1)

print(Solution().lcaDeepestLeaves(n3))
