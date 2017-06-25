"""
    264. Ugly Number II

    Solution from BianChengZhiMei
    @date: 2017/06/19
"""
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        i2 = 0
        i3 = 0
        i5 = 0
        res = [1 for i in xrange(n)]
        i = 1
        while i < n:
            res[i] = min(min(res[i2]*2, res[i3]*3), res[i5]*5)
            while res[i2]*2 <= res[i]:
                i2 += 1
            while res[i3]*3 <= res[i]:
                i3 += 1
            while res[i5]*5 <= res[i]:
                i5 += 1
            i += 1
        return res[n - 1]