"""
	231. Power of Two

	@date: 2017/02/03
"""
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        return n & (n - 1) == 0