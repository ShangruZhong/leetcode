"""
    52. N-Queens II 

    @date: 2016/11/17
"""
class Solution(object):
    def __init__(self):  
        self.count = 0
        
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        def check(k,j):  
            for i in range(k):  
                if board[i] == j or abs(k-i) == abs(board[i]-j):  
                    return False  
            return True
            
        def backtracking(depth):  
            if depth == n:  
                self.count += 1  
                return  
            for i in range(n):  
                if check(depth, i):  
                    board[depth] = i  
                    s = '.'*n  
                    backtracking(depth + 1)  
        board=[-1 for i in range(n)]  
        backtracking(0)  
        return self.count  