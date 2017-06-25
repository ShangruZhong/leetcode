"""
    343. Integer Break

    Important !!!
    @date: 2017/06/18
"""
class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in xrange(n + 1)]
        dp[1] = 1
        for i in xrange(2, n + 1):
            for j in xrange(1, i):
                dp[i] = max(dp[i], max(j, dp[j])*max(i - j, dp[i - j]))
        return dp[n]