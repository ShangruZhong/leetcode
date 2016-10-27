"""
    89. Gray Code

    Directly transform: binary -> gray
    G(n) = B(n)/2 XOR B(n)
    @date: 2016/10/27
"""
class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        num = 1 << n
        result = []
        for i in xrange(num):
            result.append((i >> 1) ^ i)
        return result