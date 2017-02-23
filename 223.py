"""
    233. Number of Digit One

    @date: 2017/02/23
"""
class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        ones = 0
        m = 1
        while m <= n:
            a = n/m
            b = n%m
            ones += (a + 8)/10*m + (a%10 == 1)*(b + 1)
            m *= 10
        return ones