"""
    102. Binary Tree Level Order Traversal

    Using recursion to implement level Traversal
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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.levelTraversal(root, 0, result)
        return result
    
    def levelTraversal(self, root, level, result):
        if root:
            if len(result)<level+1:  # ensure left-child and right-child in the same level
                result.append([])
            result[level].append(root.val) # level index to store value 
            self.levelTraversal(root.left, level+1, result) 
            self.levelTraversal(root.right, level+1, result)
                