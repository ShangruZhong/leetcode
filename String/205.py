"""
    205. Isomorphic Strings

    Hash map to record position of char
    @date: 2017/06/09
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        size = len(s)
        hashMap_1 = [0 for i in xrange(256)]
        hashMap_2 = [0 for i in xrange(256)]
        for i in xrange(size):
            if hashMap_1[ord(s[i])] != hashMap_2[ord(t[i])]:
                return False
            hashMap_1[ord(s[i])] = i + 1
            hashMap_2[ord(t[i])] = i + 1
        return True