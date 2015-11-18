"""
    38. Count and Say

    The ith string describes how the last string is read,
    like the 4th string "1211", the 5th string should be "one 1, one 2, two 1", as "111221".
    In short, string consists of several "count,value".

    When ask return the Nth string, should return the description of (N-1) string.

    @author: Shangru
    @date: 2015/11/15
"""
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return None
        s = str(1)
        while n>1:
            last = s
            s = []
            char = last[0]
            count = 1
            for i in range(1, len(last)):
                if last[i] == char:
                    count += 1
                else:
                    s.append(str(count))
                    s.append(char)
                    # new count
                    char = last[i]
                    count = 1
            s.append(str(count))
            s.append(char)
            n -= 1
        return "".join(s)





