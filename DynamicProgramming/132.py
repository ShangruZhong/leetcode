"""
    132. Palindrome Partitioning II

    @date: 2017/01/24
"""
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = []
        part = [[False for x in xrange(n)] for x in xrange(n)]
        for i in xrange(n + 1):
            dp.append(n - 1 - i) # dp[n] = -1
        for i in xrange(n - 1, -1, -1):
            for j in xrange(i, n):
                if s[i] == s[j] and (j - i < 2 or part[i + 1][j -1]):
                    part[i][j] = True
                    dp[i] = min(dp[i], dp[j + 1] + 1)
        return dp[0]