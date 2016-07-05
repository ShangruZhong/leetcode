"""
	3. Longest Substring Without Repeating Characters

	@date: 2016/07/02
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = 0
        lastpos = dict() # unique char last position
        for i in xrange(len(s)):
            if s[i] in lastpos and lastpos[s[i]] >= left:
                left = lastpos[s[i]] + 1 # update substring left bound
            lastpos[s[i]] = i # update last position
            if i - left + 1 > res:
                res = i - left + 1
        return res
        
