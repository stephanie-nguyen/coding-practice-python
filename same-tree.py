'''
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

'''


def isSameTree(p, q):
    return p and q and p.val == q.val and all(map(self.isSameTree, (p.left, p.right), (q.left, q.right))) or p is q

p = [1,2,3]
q = [1,2,3]
print(isSameTree(p, q))


'''
def isSameTree(self, p, q):
    def t(n):
        return n and (n.val, t(n.left), t(n.right))
    return t(p) == t(q)
'''

'''
def isSameTree(self, p, q):
    if p and q:
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
    return p is q
'''
