"""
	103. Binary Tree Zigzag Level Order Traversal

	Using bool variable to tag
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        tag = 1
        self.levelTraversal(root, 0, tag, result)
        return result
    
    def levelTraversal(self, root, level, tag, result):
        if root:
            if len(result)<level+1:  # ensure left-child and right-child in the same level
                result.append([])
            if tag: # result list sequence differs
                result[level].append(root.val) # from left to right
            else:
                result[level].insert(0,root.val) # from right to left
            tag = not tag
            self.levelTraversal(root.left, level+1, tag, result) 
            self.levelTraversal(root.right, level+1, tag, result)