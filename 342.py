"""
    342. Power of Four

    @date: 2017/06/18
"""
class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while i <= num:
            if i == num:
                return True
            else:
                i *= 4
        return False