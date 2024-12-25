from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

OR = 2
AND = 3

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if (root.left is None and root.right is None):
            return root.val == 1

        if (root.val == AND):
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        else:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)


root = TreeNode(
    OR,
    1,
    TreeNode(
        AND,

    )
)