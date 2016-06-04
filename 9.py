"""
	9. Palindrome Number

	@date: 2016/06/02
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        d = 1
        while x/d >= 10:
            d *= 10 
        while x > 0:
            q = x/d; # head
            r = x%10; # tail
            if q != r:
                return False;
            x = x%d /10;
            d /= 100 
        return True