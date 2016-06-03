"""
    7. Reverse Integer

    Check overflow(32-bit) of integer when returns
    @date: 2016/06/02
"""
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        r = 0
        flag = 1
        if x < 0:
            x = -x
            flag = -1
        while x != 0:
            r = r*10 + x%10
            x /= 10
        if r > 2**31-1 or r < - 2**31 + 1:
            return 0
        else:
            return r*flag