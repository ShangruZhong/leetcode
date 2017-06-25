"""
    290. Word Pattern
    
    Using two hashMap to record pos of chars 
    Similar to 205.
    @date: 2017/06/13
"""
class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str = str.split()
        if len(pattern) != len(str):
            return False
        hashMap_1 = {}
        hashMap_2 = {}
        for i in xrange(len(str)):
            if pattern[i] not in hashMap_1:
                hashMap_1[pattern[i]] = i
            if str[i] not in hashMap_2:
                hashMap_2[str[i]] = i
            if hashMap_1[pattern[i]] != hashMap_2[str[i]]:
                return False
        return True