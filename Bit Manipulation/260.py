"""
    260. Single Number III

    The key lies in finding the lower 1 bit position 
    @author: Shangru
    @date: 2017/01/05
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0:
            return [0, 0]
        axorb = 0
        for num in nums:
            axorb ^= num

        lower1bit = axorb - (axorb & (axorb - 1)) # 11010 -> 00010, very important 
        a, b = 0, 0
        for num in nums:
            # value at lower1bit position of a and b must be different
            if lower1bit & num == 0:
                a ^= num
            else:
                b ^= num
        return [a, b]      