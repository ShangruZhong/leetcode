"""
    125. Valid Palindrome

    Judge whether a string is palindrome, considering alphanumeric characters
    but ignoring cases.
    Notice: empty string should be judged as palindrome one.

    @author: Shangru
    @date: 2015/10/24
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        num = len(s)
        if num == 0: # if string is empty, return True
            return True
        s = s.lower()
        left = 0
        right = num-1
        print s
        while left != right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                    if left>right: # Notice! Avoid left exceeds right
                        break
                else:
                    return False
            elif s[left].isalnum():
                right -= 1
            else:
                left += 1
        return True


