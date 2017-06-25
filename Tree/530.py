"""
    530. Minimum Absolute Difference in BST
    
    Similar to 539. Minimum Time Difference
    to find the min diff of val in sorted arrays
    min_diff = min(min_diff, cur.val - prev)
    
    @date: 2017/04/27
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def __init__(self):
        self.min_diff = (1<<31) - 1
        self.prev = -1
        
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return self.min_diff
        self.getMinimumDifference(root.left)
        if self.prev >= 0:
            self.min_diff = min(self.min_diff, root.val - self.prev)
        self.prev = root.val
        self.getMinimumDifference(root.right)
        return self.min_diff
       
    
        