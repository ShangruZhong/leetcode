"""
	110. Balanced Binary Tree

	@author: Shangru
	@date: 2016/02/22
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.height(root) >= 0
        
    def height(self, root):
        if root == None:
            return 0
        left_h = self.height(root.left)
        right_h = self.height(root.right)
        if left_h < 0 or right_h < 0 or abs(left_h-right_h) > 1:
            return -1
        return max(left_h, right_h) + 1
        
        
        
        
        
        
        
        