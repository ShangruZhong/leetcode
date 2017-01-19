"""
	22. Generate Parentheses

	@date: 2016/09/15
"""
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.result = list()
        self.backtracking('', 0, 0, n)
        return self.result
        
    def backtracking(self, str, left, right, num):
        if len(str) == num*2: # n combinations contain 2n parentheses
            self.result.append(str)
            return 
        if left < num:
        	self.backtracking(str + '(', left + 1, right, num)
        if right < left and right < num:
        	self.backtracking(str + ')', left, right + 1, num)
        
s = Solution()
print s.generateParenthesis(4)