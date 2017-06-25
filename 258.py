"""
    258. Add Digits
    
    @date: 2017/05/07
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def add(num):
            s = 0
            while num:
                tmp = num % 10
                s += tmp
                num /= 10
            return s
        while num/10:
            num = add(num)
        return num