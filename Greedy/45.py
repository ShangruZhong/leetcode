"""
	45. Jump Game II

	@date: 2016/05/31
"""
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minStep = 0
        maxStep = 0
        cur = 0
        for i in xrange(len(nums)):
            if i > maxStep:
                maxStep = cur
                minStep += 1
            cur = max(cur, i + nums[i])
        return minStep