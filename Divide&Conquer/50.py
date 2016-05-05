"""
	50. Power(x,n)

	x^n = x^(n/2) * x^(n/2) * x^(n%2)
	O(log n)
"""
class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            return 1.0 / self.pow(x, -n)
        else:
            return self.pow(x, n)
            
    def pow(self, x, n):
        if n == 0:
            return 1
        sub = pow(x, n / 2)
        if n % 2 == 0:
            return sub * sub
        else:
            return sub * sub * x
