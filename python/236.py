# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        l, r = self.lowestCommonAncestor(root.left, p, q), self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            # This is the node we are looking for
            return root

        # Two cases:
        # 1. l = None and r = None, then we return None to indicate that p and q are not in this branch
        # 2. Either l or r == p/q, we return p/q to indicate that this branch contains either p and q
        return l or r
