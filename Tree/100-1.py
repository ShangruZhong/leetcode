"""
	100. Same Tree

	Using stack, iteration version
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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = []
        stack.append(p)
        stack.append(q)
        while len(stack):
            p = stack.pop()
            q = stack.pop()
            if p == None and q == None:
                continue
            if p == None or q == None:
                return False
            if p.val != q.val:
                return False
            
            stack.append(p.left)
            stack.append(q.left)
            
            stack.append(p.right)
            stack.append(q.right)
            
        return True