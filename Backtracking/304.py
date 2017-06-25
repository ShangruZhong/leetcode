"""
    304. Range Sum Query 2D - Immutable
    
    @date: 2017/06/18
"""
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            return
        rows, cols = len(matrix), len(matrix[0])
        self.cum = [[0] * cols for i in xrange(rows)]
        self.cum[0] = matrix[0]
        for i in xrange(1, rows):
            for j in xrange(cols):
                self.cum[i][j] = self.cum[i - 1][j] + matrix[i][j]
        
    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        s = 0
        if row1 == 0:
            for j in xrange(col1, col2 + 1):
                s += self.cum[row2][j] 
            return s
        for j in xrange(col1, col2 + 1):
            s += self.cum[row2][j] - self.cum[row1 - 1][j]
        return s    
    

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)