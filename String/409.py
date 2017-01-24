"""
	409. Longest Palindrome

	count the number of pairs
	@date: 2017/01/24
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        hash_map = {}
        pair = 0
        for i in s:
            if i in hash_map:
                hash_map.pop(i)
                pair += 1
            else:
                hash_map[i] = 1
        if hash_map:
            return pair*2 + 1
        else:
            return pair*2