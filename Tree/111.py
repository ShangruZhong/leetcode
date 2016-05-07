"""
	111. Minimum Depth of Binary Tree(II)
	
	Recursive
	@date: 2016/05/05
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.minDep(root, False)
        
    def minDep(self, root, hasBro):
        if not root:
            if hasBro:
                return 10**10
            else:
                return 0
        return 1 + min(self.minDep(root.left, root.right != None), \
            self.minDep(root.right, root.left != None))