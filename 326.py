"""
    326. Power of Three

    Tricks
    @date: 2017/06/19
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and 3**19 % n == 0