"""
    72. Edit Distance

    Classical DP problem
    f[i][j], the min edit dist between word1[0,i] and wword2[0,j]
    suppose the last char of word1 and word2 are c and d:
    if c == d:
        f[i, j] = f[i-1, j-1]
    else:
        if replace c with d: f[i, j] = f[i-1, j-1] + 1
        if apepend d after c: f[i, j] = f[i, j-1] + 1
        if remove c: f[i][j] = f[i-1, j] + 1
        
    @date: 2016/11/21
"""
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len1, len2 = len(word1), len(word2)
        f = [[0]*(len2 + 1) for _ in xrange(len1 + 1)] # f[n + 1][m + 1]
        
        for i in xrange(len1 + 1):
            f[i][0] = i
        for j in xrange(len2 + 1):
            f[0][j] = j
        for i in xrange(1, len1 + 1):
            for j in xrange(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    f[i][j] = f[i - 1][j - 1] # case 1
                else:
                    minval = min(f[i - 1][j], f[i][j - 1])
                    f[i][j] = min(f[i - 1][j - 1], minval) + 1
        return f[len1][len2]