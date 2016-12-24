"""
    90. Subsets II

    @date: 2016/12/24
"""
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        nums.sort()
        res = []
        self.backtracking(nums, 0, [], res)
        return res
    
    def backtracking(self, nums, depth, path, res):
        res.append(path)
        for i in xrange(depth, len(nums)):
            if i > depth and nums[i] == nums[i - 1]:
                continue
            self.backtracking(nums, i + 1, path + [nums[i]], res)