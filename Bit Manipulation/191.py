"""
    191. Number of 1 Bits

    @date: 2017/02/03
"""
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count