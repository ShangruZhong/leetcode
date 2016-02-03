"""
    145. Binary Tree Postorder Traversal

    Postorder: left-right-root = reverse(root-right-left)
    Using two stacks, first for inv-preorder(root-r-l), second for reverse output 
    @author: Shangru
    @date: 2016/02/03
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        reverse = []
        result = []
        if root == None:
            return result
        stack.append(root) 
        while len(stack):
            p = stack.pop() # 'stack' for inv-preorder 
            reverse.append(p.val) # 'reverse' to record result of inv-preorder
            if p.left:
                stack.append(p.left)
            if p.right:
                stack.append(p.right)
        while len(reverse): 
            result.append(reverse.pop())
        return result 