"""
    242. Valid Anagram

    string sort...
    @date: 2017/02/24
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s) and not len(t):
            return True
        elif len(s) != len(t):
            return False
        ls, lt = list(s), list(t)
        ls.sort()
        lt.sort()
        for i in xrange(len(s)):
            if ls[i] != lt[i]:
                return False
        return True