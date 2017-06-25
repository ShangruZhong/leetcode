"""
    543. Diameter of Binary Tree

    Similar to 124. Binary Tree Maximum Path Sum
    @date: 2017/04/24
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.max_path = 0
        
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        # max_path = 0
        self.dfs(root)
        return self.max_path
        
    def dfs(self, node):
        if not node:
            return 0
        left_depth = self.dfs(node.left)
        right_depth = self.dfs(node.right)
        self.max_path = max(self.max_path, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)
        
        