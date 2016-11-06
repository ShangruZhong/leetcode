"""
    78. Subsets

    @date: 2016/11/01
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = list()
        path = list()        
        self.backtracking(nums, len(nums), path, res)
        return res

    def backtracking(self, nums, k, path, res):
        if k == 0:
            res.append(path)
            return res
        self.backtracking(nums[1:], k - 1, path + [nums[0]], res)
        self.backtracking(nums[1:], k - 1, path, res) # don't save current nums[0] to path
