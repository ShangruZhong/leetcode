"""
    199. Binary Tree Right Side View

    Level Traversal, using for loop to find right-most
    @date: 2017/06/07
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root:
            return res
        queue = []
        queue.append(root)
        while queue:
            size = len(queue)
            for i in xrange(size):
                node = queue.pop(0)
                if i == size - 1:
                    res.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return res
            