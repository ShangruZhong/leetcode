"""
    468. Validate IP Address

    @date: 2017/02/04
"""
class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        string = IP.split('.')
        if len(string) == 4:
            for i in xrange(len(string)):
                if not (string[i].isdigit() and 0 <= int(string[i]) < 256) or (string[i][0] == '0' and len(string[i]) > 1):
                    return "Neither"
            return "IPv4"
        
        string = IP.split(':')
        if len(string) == 8:
            for i in xrange(len(string)):
                if not (self.is_hex(string[i]) and len(string[i]) <= 4):
                    return "Neither"
            return "IPv6"
        return "Neither"
                    
    
    def is_hex(self, string):
        if not len(string):
            return False
        hex_digits = set('0123456789abcdefABCDEF')
        for s in string:
            if s not in hex_digits:
                return False
        return True