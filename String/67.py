"""
    67. Add Binary

    @author: Shangru
    @date: 2015/10/28
"""
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        alen = len(a)
        blen = len(b)
        if alen > blen:
            b = '0' * (alen - blen) + b
            length = alen
        else:
            a = '0' * (blen - alen) + a
            length = blen
        a = a[::-1]
        b = b[::-1]
        Sum = ''
        carry = 0
        for i in xrange(length):
            tmp = ord(a[i]) - 48 + ord(b[i]) - 48 + carry
            Sum += str(tmp % 2)
            carry = tmp / 2
        if carry == 1:
            Sum += '1'
        return Sum[::-1]