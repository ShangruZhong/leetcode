"""
    53. Maximum Subarray

    Classical DP problem
    sum[i] = max(sum[i - 1] + nums[i], nums[i])
    @date: 2016/11/20
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not len(nums):
            return 0
        s = nums[0]
        smax = nums[0]
        for i in xrange(1, len(nums)):
            s = max(s + nums[i], nums[i])
            if s > smax:
                smax = s
        return smax