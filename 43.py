"""
    43. Multiply Strings
    
    Large number multiplication
    @date: 2016/11/20
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        len1, len2 = len(num1), len(num2)
        num1 = num1[::-1] # reverse
        num2 = num2[::-1]
        raw_res = [0 for _ in xrange(len1 + len2)]
        res = []
        for i in xrange(len1):
            for j in xrange(len2):
                raw_res [i + j] += int(num1[i]) * int(num2[j])

        for i in xrange(len1 + len2):
            digit = raw_res[i] % 10
            carry = raw_res[i] / 10
            if i < len1 + len2 - 1:
                raw_res[i + 1] += carry # add carry to next digit
            res.append(str(digit)) # save final digit at current position
        res.reverse()
        while res[0] == '0' and len(res) > 1:
            del res[0]
        return "".join(res) # list->str