"""
    214. Shortest Palindrome

    Brute force solution, why not KMP?
    @date: 2017/01/24
"""
class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        reverse = s[::-1]
        for i in xrange(len(s) + 1):
            if s.startswith(reverse[i:]):
            # if self.startwith(s, reverse[i:]):
                return reverse[:i] + s
                
    def startwith(self, s, prefix):
        """
        Implement string.startswith(prefix)
        but O(|prefix|)
        
        if prefix == None, 
        also return True
        """
        if len(s) < len(prefix):
            return False
        l, r = 0, len(prefix) - 1
        while l <= r:
            if s[l] != prefix[l] or s[r] != prefix[r]:
                return False
            else:
                l += 1
                r -= 1
        return True