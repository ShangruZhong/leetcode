"""
    537. Complex Number Multiplication

    @date: 2017/04/27
"""
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = self.complex2int(a)
        b = self.complex2int(b)
        return str(a[0]*b[0]-a[1]*b[1]) + '+' + str(a[0]*b[1]+a[1]*b[0]) + 'i'
        
        
    def complex2int(self, a):
        a = a.strip('i').split('+')
        a = [int(i) for i in a]
        return a
    