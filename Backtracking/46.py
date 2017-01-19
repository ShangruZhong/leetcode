"""
	46. Permutations

    Given [1,2,3], return all the permutations
	Backtracking & Enumeration
	@date: 2016/10/07
"""
class Solution(object):
    def permute(self, nums):
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
        for i in xrange(len(nums)):
            # foreach sub-node of nums[i], the rest exclude nums[i]
            rest = nums[:i] + nums[i + 1:]
            self.backtracking(rest, path + [nums[i]], res)