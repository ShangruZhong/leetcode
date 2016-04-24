"""
	108.Convert Sorted Array to Binary Search Tree
	
	Binary search & recursion
	@date: 2016/04/24
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.toBST(nums, 0, len(nums)-1)
    
    def toBST(self, nums, first, last):
        if first > last:
            return None 
        mid = first + (last - first) / 2
        root = TreeNode(nums[mid])
        root.left = self.toBST(nums, first, mid - 1)
        root.right = self.toBST(nums, mid + 1, last)
        return root
