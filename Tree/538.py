"""
    538. Convert BST to Greater Tree
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.s = 0
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return 
        self.addSum(root)
        return root
    
    def addSum(self, node):
        if not node:
            return
        self.addSum(node.right)
        node.val += self.s
        self.s = node.val
        self.addSum(node.left)
        return
        
            
            