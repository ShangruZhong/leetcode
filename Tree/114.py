"""
	114. Flatten Binary Tree to Linked List

	@author: Shangru
	@date: 2016/02/23
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root == None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left == None:
            return
        p = root.left
        while p.right:
            p = p.right
        p.right = root.right
        root.right = root.left
        root.left = None
        