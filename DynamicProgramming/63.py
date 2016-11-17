"""
    63. Unique Paths II

    modified by 62.py
    @date: 2016/11/17
"""
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[0][0] or obstacleGrid[m - 1][n - 1]: # start or finish obstacle
            return 0
        
        f = [0] * n
        if not obstacleGrid[0][0]: # no obstacle
            f[0] = 1
        else:
            f[0] = 0
            
        for i in xrange(m):
            for j in xrange(n):
                if not obstacleGrid[i][j]: #  no obstacle
                    if not j:
                        f[j] == 0
                    else:
                        f[j] = f[j - 1] + f[j]
                else:
                    f[j] = 0
                    
        return f[n - 1]