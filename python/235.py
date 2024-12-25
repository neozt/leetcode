# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        smaller_val = p.val if p.val < q.val else q.val
        larger_val = p.val if p.val > q.val else q.val

        if smaller_val <= root.val and larger_val >= root.val:
            return root
        elif larger_val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return self.lowestCommonAncestor(root.right, p, q)