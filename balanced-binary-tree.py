'''
Given a binary tree, determine if it is height-balanced.
For this problem, a height-balanced tree is defined as a binary tree in which the left and right subtrees of every node differ in height by no more than 1

Example:
  Input: root = [3,9,20,null,null,15,7]
  Output: true
  
Example:
  Input: root = [1,2,2,3,3,null,null,4,4]
  Output: false
'''


import pdb

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        leftheight=self.height(root.left)
        rightheight=self.height(root.right)
        #print(leftheight,rightheight)
        if abs(leftheight-rightheight)<=1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False

    def height(self, root):
        #breakpoint()
        #print(root)
        if not root:
            return 0
        
        leftheight=self.height(root.left)
        rightheight=self.height(root.right)
        #print(leftheight,rightheight)
        return max(leftheight,rightheight)+1
'''
    def printBalance(self, root):
        #print(root.val, root.left.val, root.right.val)
        return root.val, root.left.val, root.right.val
def isBalanced(root):
    print(root)
    return root
'''


#a = TreeNode(val=3,left=TreeNode(val=9,left=None, right=None), right=TreeNode(val=20,left=TreeNode(val=15),right=TreeNode(val=7)))
#a = TreeNode(val=1,left=TreeNode(val=2,left=TreeNode(val=3,left=TreeNode(val=4),right=TreeNode(val=4)), right=TreeNode(val=3)), right=TreeNode(val=2,left=None,right=None))
a = TreeNode(val=1,left=TreeNode(val=2,left=TreeNode(val=3)))


#pdb.set_trace()
b = Solution()
print(b.isBalanced(a))

