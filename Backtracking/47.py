"""
	47. Permutations II

	remove sub-node if it has occured on the same level
	@date: 2016/10/07
"""
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.backtracking(nums, [], res)
        return res
        
    def backtracking(self, nums, path, res):
        if not nums:
            res.append(path)
        unique = []
        for i in xrange(len(nums)):
            # foreach sub-node of nums[i], the rest exclude nums[i]
            if nums[i] not in unique: 
                unique.append(nums[i])
                rest = nums[:i] + nums[i + 1:]
                self.backtracking(rest, path + [nums[i]], res)