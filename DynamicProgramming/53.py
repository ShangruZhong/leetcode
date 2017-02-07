"""
    53. Maximum Subarray

    if dp[i-1] > 0: dp[i] = dp[i-1]+nums[i]
    else: dp[i] = nums[i]
    @date: 2017/02/07
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return nums
        dp = [0]*len(nums)
        dp[0] = nums[0]
        for i in xrange(1, len(nums)):
            dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)
        return max(dp)