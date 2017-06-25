"""
    216. Combination Sum III

    classical dfs quetions
    @date: 2017/06/10
"""
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(nums, k, diff, path):
            if k == 0 and diff == 0:
                res.append(path)
                return
            for i in xrange(len(nums)):
                if diff < nums[i]:
                    return
                dfs(nums[i+1:], k - 1, diff - nums[i], path + [nums[i]])
        nums = range(1, 10)
        dfs(nums, k, n, [])
        return res