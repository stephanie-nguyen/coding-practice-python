'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

'''
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#class Solution:
#     def isSameTree(self, p, q):
#         return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q

# class Solution:
#     def isSameTree(self, p, q):
#         def t(n):
#             return n and (n.val, t(n.left), t(n.right))
#         return t(p) == t(q)

class Solution:
    def isSameTree(self, p, q):
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q


p = TreeNode(val=1, left=2, right=3)
q = TreeNode(val=1, left=2, right=3)
b = Solution()
print(b.isSameTree(p,q))
