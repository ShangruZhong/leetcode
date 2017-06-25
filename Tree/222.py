"""
    222. Count Complete Tree Nodes

    @date: 2017/06/10
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        lftCount = rgtCount = 0
        lftNode = root
        rgtNode = root
        while lftNode:
            lftCount += 1
            lftNode = lftNode.left
        while rgtNode:
            rgtCount += 1
            rgtNode = rgtNode.right
        if lftCount == rgtCount:
            return pow(2, lftCount) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)