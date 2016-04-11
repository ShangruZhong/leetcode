"""
	96. Unique Binary Search Trees

	Dynamic Planning Problem
	f[i] = sum[f(k-1)*f(i-k)], k = 1 to i
	return f[n]
	@date: 2016/04/11
"""
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # f = range(0, n+1)
        f = [0]*(n+1)
        f[0], f[1] = 1, 1
        for i in xrange(2, n+1):
        	for k in xrange(1, i+1):
        		f[i] += f[k-1]*f[i-k]
        return f[n]
