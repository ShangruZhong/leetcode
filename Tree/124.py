"""
    124. Binary Tree Maximum Path Sum
    
    Similar to 543. Diameter of Binary Tree, DFS
    @date: 2017/04/29
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.maxValue = - (1<<31) + 1
    
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.maxValue
        
    def dfs(self, node):
        if not node:
            return 0
        leftValue = max(0, self.dfs(node.left))
        rightValue = max(0, self.dfs(node.right))
        self.maxValue = max(self.maxValue, node.val + leftValue + rightValue)
        return node.val + max(leftValue, rightValue)