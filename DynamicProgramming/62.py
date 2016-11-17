"""
    62. Unique Paths

    backtracking: straight-forward solution, but exceeds time limit
    dp: f[i][j] = f[i - 1][j] + f[i][j - 1], O(mn)
    @date: 2016/11/17
"""
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        f = [0] * n
        f[0] = 1
        for i in xrange(m):
            for j in xrange(1, n):
                f[j] = f[j - 1] + f[j]
        return f[n - 1]