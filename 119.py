"""
	119. Pascal's Triangle II

	Recursive version also exceeds time limits
	Using recursion of combination number C(n,k), 
	C(n, k) = n(n-1)...(n-k+1)/k(k-1)...1
	C(n, k-1) = n(n-1)...(n-k+2)/(k-1)(k-2)...1
	=>C(n, k) = C(n, k-1)*(n-k+1)/k
	@date: 2016/09/14
"""
class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex < 0:
            return [1]
        each = [1]*(rowIndex + 1)
        for i in xrange(1, rowIndex):
            each[i] = each[i - 1]*(rowIndex - i + 1)/i
        return each

# Naive solution
# class Solution(object):
#     def getRow(self, rowIndex):
#         """
#         :type rowIndex: int
#         :rtype: List[int]
#         """
#         if rowIndex <= 0:
#             return [1]
#         if rowIndex == 1:
#             return [1,1]
#         else:
#             each = [1]*(rowIndex+1)
#             i = 1
#             while i < rowIndex:
#                 each[i] = (self.getRow(rowIndex-1))[i-1] + (self.getRow(rowIndex-1))[i]
#                 i += 1
#             return each