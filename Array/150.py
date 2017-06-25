"""
   150. Evaluate Reverse Polish Notation
   
   pay attention to the division in python
   @date: 2017/05/07
"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if t == '*':
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(op1*op2)
            elif t == '+':
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(op1 + op2)
            elif t == '-':
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                stack.append(op2 - op1)
            elif t == '/':
                op1 = int(stack.pop())
                op2 = int(stack.pop())
                if op2*op1 < 0 and op2%op1 != 0: # op2&op1 -> pos&neg
                    stack.append(op2/op1 + 1) # 6/-132 = 0 not -1
                else:
                    stack.append(op2/op1)
            else:
                stack.append(t)
        return int(stack[-1])