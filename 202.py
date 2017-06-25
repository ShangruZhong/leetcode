"""
    202. Happy Number
    
    similar to linked list, slow & fast pointer to find loop
    @date: 2017/05/17
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 1 and n < 7:
            return False
        def squareSum(n):
            s = 0
            while n:
                tmp = n%10
                s += tmp*tmp
                n /= 10
            return s
        slow = fast = n
        while slow > 1:
            slow = squareSum(slow)
            if slow == 1:
                return True
            fast = squareSum(squareSum(fast))
            if fast == 1:
                return True
            if slow == fast:
                return False
        return True
