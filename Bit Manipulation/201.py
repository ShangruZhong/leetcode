"""
    201. Bitwise AND of Numbers Range

    a little confused
    @date: 2017/02/21
"""
class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        while m < n:
            n &= n - 1
            print n
        return m & n

    # solution 2
    def rangeBitwiseAnd(self, m, n):
        move_factor = 1
        while m != n:
            m >>= 1
            n >>= 1
            move_factor <<= 1
        return m*move_factor