# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        self.preorder = preorder
        self.postorder_map = {val: i for i, val in enumerate(postorder)}
        self.index = 0

        return self.build_tree(None)


    def build_tree(self, parent: Optional[int]):
        if self.index == len(self.preorder):
            return None

        candidate = self.preorder[self.index]
        if (
                parent is None
                or self.postorder_map[candidate] < self.postorder_map[parent] # Check if candidate is child of parent
        ):
            self.index += 1
            return TreeNode(
                candidate,
                self.build_tree(candidate),
                self.build_tree(candidate)
            )

        return None

print(Solution().constructFromPrePost([1,2,4,5,3,6,7], [4,5,2,6,7,3,1]))