"""
	98. Validate Binary Search Tree

	Bounder: (max_integer, min_integer) = (10**10, -10**10)
	@author: Shangru
	@date: 2016/04/13
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValid(root, -10**10, 10**10)
        
    def isValid(self, root, min, max):
        if not root:
            return True
        if root.val <= min or root.val >= max:
            return False
        return self.isValid(root.left, min, root.val) and self.isValid(root.right, root.val, max)