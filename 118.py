"""
	118. Pascal's Triangle

	@date: 2016/09/14
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows <= 0:
            return []
        all = []
        for i in xrange(numRows):
            each = [1]*(i + 1)
            j = 1
            while j <= i - 1:
                each[j] = all[i-1][j-1] + all[i-1][j]
                j += 1
            all.append(each)
        return all