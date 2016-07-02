"""
	5. Longest Palindromic Substring

	@date: 2016/07/01
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        resleft, resright, maxval = 0, 1, 0
        length = len(s)
        for i in range(1, length * 2):
            if i & 1 : # i = 1, 3, 5, ...
                left = i / 2 
                right = left
            else : # i = 2, 4, 6
                left = i / 2 - 1
                right = left + 1
            while (left >= 0) and (right < length) and (s[left] == s[right]):
                left -= 1
                right += 1
            left += 1
            right -= 1
            if right - left > maxval: # update tmp result
                maxval = right - left
                resleft = left
                resright = right
        return s[resleft: resright + 1]