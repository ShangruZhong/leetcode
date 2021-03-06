"""
    345. Reverse Vowels of a String

    @date: 2017/06/18
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and s[l].lower() not in vowels:
                l += 1
            while l < r and s[r].lower() not in vowels:
                r -= 1
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)