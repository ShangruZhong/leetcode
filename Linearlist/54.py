"""
    54. Spiral Matrix

    @date: 2016/12/07
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        rows = len(matrix)
        cols = len(matrix[0])
        beginRows, beginCols = 0, 0
        endRows, endCols = rows, cols
        result = list()
        while 1:
            for j in xrange(beginCols, endCols):
                result.append(matrix[beginRows][j])
            beginRows += 1
            if beginRows >= endRows:
                break
            
            for i in xrange(beginRows, endRows):
                result.append(matrix[i][endCols - 1])
            endCols -= 1
            if endCols <= beginCols:
                break

            for j in xrange(endCols - 1, beginCols - 1, -1):
                result.append(matrix[endRows - 1][j])
            endRows -= 1
            if endRows <= beginRows:
                break

            for i in xrange(endRows - 1, beginRows - 1, -1):
                result.append(matrix[i][beginCols])
            beginCols += 1
            if beginCols >= endCols:
                break
        return result