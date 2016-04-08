"""
	105. Construct Binary Tree from Preorder and Inorder Traversal

	# Building Binary Tree

	@author: Shangru
	@date: 2016/04/08
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder: 
            return None
        first = preorder.pop(0)
        node = TreeNode(first)
        i = inorder.index(first)
        node.left = self.buildTree(preorder, inorder[0:i])
        node.right = self.buildTree(preorder,inorder[i+1:])
        return node 