"""
    120. Triangle

    Similar to 64. Minimum Path Sum
    DP accepted but need O(n^2) auxiliary space

    @author: Shangru
    @date: 2017/01/06
"""
class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        level = len(triangle)
        if level == 0:
            return 0
        
        dp = [[0]*(i + 1) for i in xrange(level)]
        dp[0][0] = triangle[0][0]
        
        for i in xrange(1, level):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
        
        for i in xrange(1, level):
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]
            
        for i in xrange(2, level):
            for j in xrange(1, i):
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j]) + triangle[i][j]
        
        return min(dp[level - 1])