"""
    547. Friend Circles

    @date: 2017/04/24
"""
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited = [0 for i in xrange(len(M))]
        count = 0
        for i in xrange(len(M)):
            if not visited[i]:
                visited[i] = 1
                self.dfs(M, i, visited)
                count += 1
        return count
        
    def dfs(self, M, i, visited):
        """
        check each node j in M for i 
        """
        for j in xrange(len(M)):
            if M[i][j] == 1:
                if not visited[j]:
                    visited[j] = 1
                    self.dfs(M, j, visited)
        return