"""
    String to Integer (atoi)

    @author: Shangru
    @date: 2016/06/07
"""
import sys
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip() # remove space
        if str == "":
            return 0
        index = 0
        sign = 1 # postive or negative
        res = 0
        Max = (1 << 31) - 1 # 2147483647
        if str[index] == '+':
            index += 1
        elif str[index] == '-':
            index += 1
            sign = -1 # negative
        
        for i in xrange(index, len(str)):
            if str[i] < '0' or str[i] >'9':
                break
            res = res*10 + int(str[i])
            if res > sys.maxint: # sys.maxint = 2147483647
                break
        res *= sign
        if res >= Max:
            return Max
        if res < - Max:
            return - Max - 1
        return res    
        