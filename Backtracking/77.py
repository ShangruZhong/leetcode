"""
    77. Combinations

    Similar to Permutation (47)
    Backtracking
    @date: 2016/11/01
"""
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = list()
        path = list()
        return self.backtracking(range(1, n+1), k, path, res)

    def backtracking(self, nums, k, path, result):
        if k == 0:
            res.append(path)
        if len(nums) >= k: # improve recursion
            for i in xrange(len(nums)):
                self.backtracking(nums[i+1:], k - 1, path + [nums[i]], res)
        return res