"""
    172. Factorial Trailing Zeroes

    calculate number of factor 5
    n /= 5 --> log time complexity
    @date: 2017/05/11
"""
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n:
            count += n / 5
            n /= 5
        return count