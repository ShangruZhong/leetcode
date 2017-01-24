"""
    131. Palindrome Partitioning

    backtracking + isPalindrome
    @date: 2017/01/24
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        path = []
        self.backtracking(0, s, path, res)
        return res
        
    def backtracking(self, index, s, path, res):
        if index == len(s):
            res.append(path)
            return
        for i in xrange(index, len(s)):
            if self.isPalindrome(s, index, i):
                self.backtracking(i + 1, s, path + [s[index : i + 1]], res)
    
    def isPalindrome(self, s, start, end):
        while start <= end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                return False
        return True