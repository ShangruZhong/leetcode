"""
    59. Spiral Matrix II

    @date: 2016/12/07
"""
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0:
            return []
        matrix = [[0] * n for i in xrange(n)]
        
        beginRows, beginCols = 0, 0
        endRows, endCols = n, n
        a = 0
        while 1:
            for j in xrange(beginCols, endCols):
                a += 1
                matrix[beginRows][j] = a
            beginRows += 1
            if beginRows >= endRows:
                break
            
            for i in xrange(beginRows, endRows):
                a += 1
                matrix[i][endCols - 1] = a
            endCols -= 1
            if endCols <= beginCols:
                break

            for j in xrange(endCols - 1, beginCols - 1, -1):
                a += 1
                matrix[endRows - 1][j] = a
            endRows -= 1
            if endRows <= beginRows:
                break

            for i in xrange(endRows - 1, beginRows - 1, -1):
                a += 1
                matrix[i][beginCols] = a
            beginCols += 1
            if beginCols >= endCols:
                break
        return matrix