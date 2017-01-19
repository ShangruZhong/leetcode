"""
    79. Word Search

    Search word horizontally or vertically in the grid
    @date: 2016/11/01
"""
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        visited = [([0] * n) for i in range(m)] # !!!: initial 2d matrix, avoid shallow copy
        for i in xrange(m):
            for j in xrange(n):
                if self.backtracking(board, word, 0, i, j, visited):
                    return True
        return False

    def backtracking(self, board, word, word_index, x, y, visited):
        """
        @params:
            word_index: character index of word
            <x, y>: location of point in board
            visited: flag 
        """
        if word_index == len(word):
            return True # success
        if x < 0 or y < 0 or x >= len(board) or y >= len(board[0]):
            return False # out of border
        if visited[x][y]:
            return False # have visited, cut
        if board[x][y] != word[word_index]:
            return False
        visited[x][y] = 1
        res = self.backtracking(board, word, word_index + 1, x - 1, y, visited) or \
            self.backtracking(board, word, word_index + 1, x, y + 1, visited) or \
            self.backtracking(board, word, word_index + 1, x + 1, y, visited) or \
            self.backtracking(board, word, word_index + 1, x, y - 1, visited)
        # if true return directly, pruning to reduce complexity, otherwise exceeds time limit
        visited[x][y] = 0
        return res

s = Solution()
print s.exist(["ABCE","SFCS","ADEE"],"ABCCED")