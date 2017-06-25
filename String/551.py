"""
    551. Student Attendance Record I

    @date: 2017/04/21
"""
class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """

        size = len(s)
        if not size:
            return
        countA = 0
        countcL = 0
        
        for i in xrange(size):
            if s[i] == 'A':
                countA += 1
                countcL = 0
            elif s[i] == 'L':
                countcL += 1
            else:
                countcL = 0
            if countA > 1 or countcL > 2:
                return False
        return True
                