"""
    73. Set Matrix Zeroes

    Straight-forward
    @date: 2016/11/17
"""
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        for i in xrange(m):
            for j in xrange(n):
                if not matrix[i][j]:
                    for k in xrange(m):
                        if matrix[k][j] != 0:
                            matrix[k][j] = 'z'
                    for k in xrange(n):
                        if matrix[i][k] != 0:
                            matrix[i][k] = 'z'
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == 'z':
                    matrix[i][j] = 0