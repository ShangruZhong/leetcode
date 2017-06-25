"""
    168. Excel Sheet Column Title
    
    'z' -> 26, 'AA' -> 27
    @date: 2017/05/11
"""
class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        res = []
        
        while n > 0:
            n -= 1
            res.append(char[n % 26])
            n /= 26
        res = list(reversed(res))
        return "".join(res)