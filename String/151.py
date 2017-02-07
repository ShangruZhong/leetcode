"""
    151. Reverse Words in a String

    reverse string
    1. reverse each word
    2. reverse the whole seq
    @date: 2017/02/04
"""
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not len(s):
            return s
        words = s.split()
        for i in xrange(len(words)):
            w = words[i]
            words[i] = self.reverse(w, 0, len(w) - 1)
        s = ' '.join(words)
        return self.reverse(s, 0, len(s) - 1)
        
    def reverse(self, s, l, r):
        s = list(s)
        while l < r:
            s[r], s[l] = s[l], s[r]
            l += 1
            r -= 1
        return ''.join(s)

    # solution 2
    def reverseWords(self, s):
        return " ".join(s.strip().split()[::-1])