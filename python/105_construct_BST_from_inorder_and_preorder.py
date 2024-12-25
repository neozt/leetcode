# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def create_node(preorder: deque[int], inorder: List[int]):
            if not preorder or not inorder:
                return None

            head = TreeNode(preorder.popleft())
            middle = inorder.index(head.val)
            head.left = create_node(preorder, inorder[:middle])
            head.right = create_node(preorder, inorder[middle + 1:])

            return head

        return create_node(deque(preorder), inorder)


print(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))