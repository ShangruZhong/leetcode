"""
    51. N-Queens

    classical DFS problem
    @date: 2016/11/07
"""
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def check(k,j,board):  
            for i in range(k):  
                if board[i] == j or abs(k-i) == abs(board[i] - j):  
                    return False  
            return True
            
        def backtracking(depth, board, valuelist, solution):  
            if depth == len(board):  
                solution.append(valuelist)  
            for row in range(len(board)):  
                if check(depth,row,board):  
                    s = '.' * len(board)  
                    board[depth] = row  
                    backtracking(depth + 1, board, valuelist + [s[:row] + 'Q' + s[row + 1:]], solution)
                    
        board = [-1 for i in range(n)]  
        solution = []  
        backtracking(0, board, [], solution)  
        return solution  