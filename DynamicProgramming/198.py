"""
    198. House Robber
    
    dp[i] = max(dp[i-2] + nums[i], dp[i-1])
    @date: 2017/05/11   
"""
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if not size:
            return 0
        dp = size*[0]
        dp[0] = nums[0]
        for i in xrange(1, size):
            if i == 1:
                dp[i] = max(nums[i], dp[0])
            else:
                dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[size - 1]