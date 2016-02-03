"""
	94. Binary Tree Inorder Traversal

	Using stack to record left-child of TreeNode, O(n)
	@author: Shangru
	@date: 2016/02/03
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
      	p = root
      	while p != None or len(stack):
      		if p != None:
      			stack.append(p)  # left->left...in stack
      			p = p.left 
      		else:
      			p = stack.pop()
      			result.append(p.val)
      			p = p.right
      	return result

      		

