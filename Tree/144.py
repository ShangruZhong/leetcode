"""
	144. Binary Tree Preorder Traversal
	
	Using stack, root, seq(right, left) 
	@author: Shangru
	@date: 2016/02/02
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[class Solution(object):
		"""
        result = []
        stack = []
        if root == None:
            return result
        stack.append(root)
        while len(stack):
            p = stack.pop()
            result.append(p.val)
            if p.right:
                stack.append(p.right)
            if p.left:
                stack.append(p.left)
        return result

# root = TreeNode(1)
# root.right = TreeNode(2)
# root.right.left = TreeNode(3)
# s = Solution()
# print s.preorderTraversal(root)
