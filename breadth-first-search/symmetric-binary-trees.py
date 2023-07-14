"""
https://leetcode.com/problems/symmetric-tree/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_symmetric(root: Optional[TreeNode]) -> bool:

    def isSymmetric(l, r) -> bool:
        if not l and not r:
            return True
        if not l or not r:
            return False
        return l.val == r.val and isSymmetric(l.left, r.right) and isSymmetric(l.right, r.left)

    if not root:
        return True
    return isSymmetric(root.left, root.right)






