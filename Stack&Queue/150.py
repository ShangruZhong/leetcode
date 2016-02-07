"""
	150. Evaluate Reverse Polish Notation

	@author: Shangru
	@date: 2016/02/02
"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for i in xrange(len(tokens)):
        	if tokens[i] == '*':
        		op1 = int(stack.pop())
        		op2 = int(stack.pop())
        		stack.append(op1*op2)
        	elif tokens[i] == '+':
        		op1 = int(stack.pop())
        		op2 = int(stack.pop())
        		stack.append(op1+op2)
        	elif tokens[i] == '-':
        		op1 = int(stack.pop())
        		op2 = int(stack.pop())
        		stack.append(op1-op2)
        	elif tokens[i] == '/':
        		op1 = int(stack.pop())
        		op2 = int(stack.pop())
        		stack.append(op2/op1)
        	else:
        		stack.append(tokens[i])
        	print stack
        return int(stack[-1])

s = Solution()
s.evalRPN(["4", "13", "5", "/", "+"])