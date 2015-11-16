"""
    12. Integer to Roman

    @author: Shangru
    @date: 2015/11/16
"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbol = ["M", "CM", "D", "CD", "C", "XC","L", "XL", "X", "IX", "V", "IV", "I"]
        i = 0
        roman = str()
        while num:
            count = num/base[i]
            num = num%base[i]
            while count:
                roman += symbol[i]
                count -= 1
            i += 1
        return roman