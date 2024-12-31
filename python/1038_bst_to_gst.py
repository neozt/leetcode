# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        acc = 0
        def dfs(root: TreeNode):
            if root is None:
                return

            dfs(root.right)
            nonlocal acc
            acc += root.val
            root.val = acc
            dfs(root.left)

        dfs(root)

        return root


