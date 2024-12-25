# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.moves = 0
        self.calculate_excess(root)
        return self.moves

    def calculate_excess(self, root: Optional[TreeNode]):
        if (not root):
            return 0

        left_excess = self.calculate_excess(root.left)
        right_excess = self.calculate_excess(root.right)

        self.moves += abs(left_excess) + abs(right_excess)

        return root.val + left_excess + right_excess - 1
