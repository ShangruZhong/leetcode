"""
    137. Single Number II

    Naive solution
    @date: 2017/01/06    
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = dict()
        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        for k in d:
            if d[k] == 1:
                return k
        
    # ===========================================
    #     if len(nums) == 0:
    #         return 0
    #     s = 0
    #     d = [0 for i in xrange(32)]
        
    #     for num in nums:
    #         tmp = self.numToBinary(num)        
    #         for j in xrange(32):
    #             d[j] += tmp[j]
        
    #     for k in xrange(32):
    #         if d[k]%3 == 1:
    #             s += (1 << k)
    #         elif d[k]%3 !=0:
    #             return -1
    #     return s
            
    # def numToBinary(self, num):
    #     d = [0 for i in xrange(32)]
    #     for i in xrange(32):
    #         if num & (1 << i):
    #             d[i] = 1
    #     return d
    
    # ================================================
    # def addNoCarry(self, ksys1, ksys2, k):
    #     for i in xrange(len(ksys1)):
    #         ksys1[i] = (ksys1[i] + ksys2[i])%k
    #     return ksys1

    # def numberToKsys(self, num, k):
    #     ksys = [0]*32
    #     i = 0
    #     while num:
    #         ksys[i] = num%k
    #         num = num/k
    #         i += 1
    #     return ksys
            
    # def ksysToNumber(self, ksys, k):
    #     num = 0
    #     for i in xrange(len(ksys)):
    #         if ksys[i]:
    #             num += ksys[i]*(k**i)
    #     return num