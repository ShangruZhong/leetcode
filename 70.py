"""
	70. Climbing Stairs

	f(n) = f(n-1) + f(n-2), n>=2
	But recursive version will exceed time limits
	@date: 2016.09/14	
"""
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        phi = (1 + 5**0.5)/2
        return int(round(phi**(n+1)/5**0.5))