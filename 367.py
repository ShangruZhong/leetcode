"""
    367. Valid Perfect Square

    @date: 2017/06/19
"""
class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        i = 1
        while i*i < num:
            i += 1
        return True if i*i == num else False