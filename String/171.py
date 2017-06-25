"""
    171. Excel Sheet Column Number

    res = res*26 + a
    @date: 2017/05/11
"""
class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        res = 0
        for char in s:
            res = 26*res + (ord(char) - ord('A') + 1)
        return res