"""
    13. Roman to Integer

    VI: V>=I, integer = V+I
    IV: I<V, integer = V-I

    @author: Shangru
    @date: 2015/11/17
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        int = 0
        for i in range(len(s)):
            if i>0 and map[s[i-1]]<map[s[i]]:
                int += map[s[i]]-2*map[s[i-1]]
            else:
                int += map[s[i]]
        return int

