"""
	66. Plus One

	@date: 2016/09/14
"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if len(digits) == 0:
            return 0
        i = len(digits) - 1
        while i >= 0:
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
            i -= 1
    
        digits_n = [0]*(len(digits)+1)
        digits_n[0] = 1 
        return digits_n