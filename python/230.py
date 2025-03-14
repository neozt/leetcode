from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        self.result = None
        self.count = 0

        def dfs(root):
            if not root:
                return

            if self.result is not None:
                return

            dfs(root.left)
            self.count += 1
            if self.count == k:
                self.result = root.val
            dfs(root.right)

        dfs(root)
        return self.result