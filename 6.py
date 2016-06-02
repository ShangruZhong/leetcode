"""
    6. ZigZag Conversion

    @date: 2016/06/02
"""
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or len(s) <= 1:
            return s
        res = str()
        for i in xrange(numRows):
            j = 0
            index = i 
            while index < len(s):
                res += s[index] # vertical
                if i != 0 and i != numRows -1: 
                    if index + (numRows - i -1) * 2 < len(s):
                        res += s[index + (numRows - i - 1) * 2]
                j += 1
                index = (2*numRows - 2)*j + i
        return res