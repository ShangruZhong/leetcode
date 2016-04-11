"""
	95. Unique Binary Search Trees II
	
	@date: 2016/04/09
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
        	return []
        return self.generate(1, n)

    def generate(self, begin, end):
    	subtree = []
    	if begin > end:
    		subtree.append(None)
    		return subtree
    	for k in xrange(begin, end + 1):
    		leftsub = self.generate(begin, k-1)
    		rightsub = self.generate(k + 1, end)
    		for i in leftsub:
    			for j in rightsub:
    				node = TreeNode(k)
    				node.left = i
    				node.right = j
    				subtree.append(node) 
    	return subtree
    