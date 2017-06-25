"""
    230. Kth Smallest Element in a BST

    @date: 2017/06/10
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.count = None
        self.res = None
        
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root:
            return None
        self.count = k
        def inorder(root):
            if root.left:
                inorder(root.left)
            self.count -= 1
            if self.count == 0:
                self.res = root.val
                return
            if root.right:
                inorder(root.right)
                
        inorder(root)
        return self.res