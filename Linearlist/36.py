class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def isValid(x, y, tmp):
            for i in range(9):
                if board[i][y] == tmp:
                    return False
            for i in range(9):
                if board[x][i] == tmp:
                    return False
            for i in range(3):
                for j in range(3):
                    if board[(x/3)*3+i][(y/3)*3+j] == tmp:
                        return False
            return True
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                tmp = board[i][j]
                board[i][j] = 'F'
                if isValid(i,j,tmp) == False:
                    return False
                else:
                    board[i][j] = tmp
        return True

board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
a = Solution()
print a.isValidSudoku(board)