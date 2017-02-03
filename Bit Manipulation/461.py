"""
    461. Hamming Distance

    @date: 2017/02/03
"""
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        if x < 0 or y <0:
            return 0
        x = x ^ y
        count = 0
        while x:
            x &= x - 1
            count += 1
        return count