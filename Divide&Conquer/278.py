"""
    278. First Bad Version

    classical binary search
    @date: 2017/06/13
"""
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            mid = (l + r) / 2
            if not isBadVersion(mid):
                l = mid + 1
            else:
                r = mid
        return l 