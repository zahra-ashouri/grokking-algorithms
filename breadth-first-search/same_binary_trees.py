"""
https://leetcode.com/problems/same-tree/

"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True

    if not p or not q:
        return False

    if p.val == q.val:
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)


# More optimized
def is_same_tree_with_explicit_dfs(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    def dfs(l, r):
        if not l and not r:
            return True

        if not l or not r:
            return False

        if l.val == r.val:
            return dfs(l.left, r.left) and dfs(l.right, r.right)

    return dfs(p, q)


if __name__ == "__main__":
    p_left = TreeNode(2)
    q_left = TreeNode(2)
    p_right = TreeNode(3)
    q_right = TreeNode(3)
    p = TreeNode(1, p_left, p_right)
    q = TreeNode(1, q_left, q_right)
    print(isSameTree(p, q))
