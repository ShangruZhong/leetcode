"""
	Sqrt(x, n)

	@date: 2016/05/05
"""
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left, right = 1, x / 2
        if x < 2:
            return x
        while left <= right:
            mid = left + (right - left) / 2
            if x / mid > mid:
                left = mid + 1
                last_mid = mid
            elif x / mid < mid:
                right = mid - 1
            else:
                return mid
        return last_mid