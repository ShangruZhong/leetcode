"""
    93. Restore IP Addresses

    @date: 2017/02/03
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.backtracking(s, 4, [], res)
        return ['.'.join(x) for x in res]
        
    def backtracking(self, s, depth, path, res):
        if len(s) > depth*3:
            return
        if depth == 0:
            res.append(path[:])
        else:
            for i in xrange(min(3, len(s) - depth + 1)):
                if (i == 2 and int(s[:3]) > 255) or (i > 0 and s[0] == '0'): 
                    continue
                self.backtracking(s[i + 1:], depth - 1, path + [s[:i + 1]], res)