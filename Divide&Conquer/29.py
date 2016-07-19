"""
    29. Divide Two Integers

    @date: 2016/07/09
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return -1
        MAX_INT= 2**31 - 1 # 2147483647 
        MIN_INT = -2**31
        flag = (dividend < 0 and divisor > 0) or (dividend >0 and divisor < 0) # res = negative
        dividend = abs(dividend)
        divisor = abs(divisor)
        result = 0
        while dividend >= divisor:
            k = 0
            tmp = divisor
            while dividend >= tmp:
                dividend -= tmp
                result += (1 << k)
                k += 1
                tmp <<= 1
        if flag:
            result = -result
        if result < MIN_INT:
            return MIN_INT
        if result > MAX_INT:
            return MAX_INT
        return result