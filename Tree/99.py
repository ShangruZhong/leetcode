"""
    99. Recover Binary Search Tree
    
    inOrder to find the first and second wrong node, and swap their val
    @date: 2017/05/07
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.first = None
        self.seconde = None
        self.prev = TreeNode(-1<<31+1)
        
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.inOrder(root)
        self.first.val, self.second.val = self.second.val, self.first.val
    
    def inOrder(self, root):
        if not root:
            return
        self.inOrder(root.left)
        
        if not self.first and self.prev.val >= root.val: 
            # not satisfy order, should be prev.val < root.val in BST
            self.first = self.prev
        if self.first != None and self.prev.val >= root.val:
            # find the second node that not satisfy order
            self.second = root
        self.prev = root
        
        self.inOrder(root.right)
        
        
        
        