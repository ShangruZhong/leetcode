"""
	338. Counting Bits

	Cannot use HammingWeight directly for [0, 1, ..., num]
	res[i] = res[i/2] + (i%2)
	(i%2) for judge odd or even number
	@date: 2017/02/21
"""
class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = [0]*(num + 1)
        for i in xrange(1, num + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res