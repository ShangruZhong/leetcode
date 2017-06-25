"""
	129. Sum Root to Leaf Numbers

	@author: Shangru
	@date: 2016/05/10
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.dfs(root, 0)
    
    def dfs(self, root, sum):
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return sum * 10 + root.val
        return self.dfs(root.left, sum * 10 + root.val) \
            + self.dfs(root.right, sum * 10 + root.val)
        