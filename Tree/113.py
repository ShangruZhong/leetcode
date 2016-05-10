"""
    113. Path Sum II 

    Pay attention to deep copy in Python list
    
    @author: Shangru
    @date: 2016/05/10
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy

class Solution(object):

    def __init__(self):
        self.tmplist = []
        self.resultlist = []
        
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.hasPathSum(root, sum)
        return self.resultlist
        
    def hasPathSum(self, root, sum):
        if root == None:
            return 
        self.tmplist.append(root.val)
        if root.left == None and root.right == None:
            if sum == root.val:
                tmp = copy.deepcopy(self.tmplist)  # !!! if not, tmplist's change leads to resultlist's change
                self.resultlist.append(tmp)
        self.hasPathSum(root.left, sum - root.val)
        self.hasPathSum(root.right, sum - root.val)
        self.tmplist.pop()

        
        