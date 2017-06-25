"""
    257. Binary Tree Paths

    Recursive & Non-recursive!!!
    @date: 2017/06/10
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        res = []
        def preorder(root, s, res):
            if not root.left and not root.right:
                res.append(s + str(root.val))
            if root.left:
                preorder(root.left, s + str(root.val) + '->', res)
            if root.right:
                preorder(root.right, s + str(root.val) + '->', res)
        preorder(root, '', res)
        return res