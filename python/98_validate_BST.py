# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.isValid = True

        self.dfs(root)

        return self.isValid

    def dfs(self, root: Optional[TreeNode]) -> (int, int):
        if not root:
            return (float("inf"), -float("inf"))

        if not self.isValid:
            # already not valid, no need check anymore
            return (float("inf"), -float("inf"))

        left_min, left_max = self.dfs(root.left)
        right_min, right_max = self.dfs(root.right)

        if left_max >= root.val or right_min <= root.val:
            self.isValid = False

        return min(left_min, root.val), max(right_max, root.val)


