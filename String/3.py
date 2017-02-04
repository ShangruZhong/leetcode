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
        
    # update
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        left = 0
        last_pos = {}
        for i in xrange(len(s)):
            if s[i] in last_pos and last_pos[s[i]] >= left:
                left = last_pos[s[i]] + 1 # reset left
            else:
                max_len = max(max_len, i - left + 1) #  max_len
            last_pos[s[i]] = i

        return max_len