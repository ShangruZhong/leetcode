"""
	58. Length of Last Word

	@date: 2016/09/13
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        i = len(s) - 1
        count = 0
        while i >= 0: 
            if s[i] != ' ':
                count += 1
            elif count != 0:
                return count
            i -= 1
        return count
     