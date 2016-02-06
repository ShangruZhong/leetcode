"""
	101. Symmetric Tree

	Similar to '100. Same Tree'
	@author: Shangru
	@date: 2016/02/05
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.isSym(root.left, root.right)
            
    def isSym(self, leftchild, rightchild):
        if leftchild == None and rightchild == None:
            return True
        if leftchild == None or rightchild == None:
            return False
        return leftchild.val == rightchild.val \
            and self.isSym(leftchild.left, rightchild.right) \
            and self.isSym(leftchild.right, rightchild.left)
        