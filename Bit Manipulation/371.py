"""
    371. Sum of Two Integers

    add without '+' or '-', use XOR instead.
    @date: 2017/02/24
"""
class Solution(object):
    def getSum(self, a, b):
        # 32 bits Max integer, 0x7FFFFFFF 
        MAX = 1 << 31 - 1
        # 32 bits Min interger, 0x80000000
        MIN = -(1 << 31)
        # mask to get last 32 bits
        mask = 0xFFFFFFFF

        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        
        return a if a <= MAX else ~(a ^ mask)