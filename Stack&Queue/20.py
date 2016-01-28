"""
	20. Valid Parentheses
	
	Using stack to judge Parentheses Matching Problem
	@author: Shangru
	@date: 2015/11/02
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """ 
     	if s == "":
        	return True   
        stack = []
       	for ch in s:
       		if ch == '(' or ch == '[' or ch == '{':
       			stack.append(ch)
       		elif len(stack)>0:
       			top = stack[-1]
       			if ch == ')' and top == '(':
       				stack.pop()
       			elif ch == ']' and top == '[':
       				stack.pop()
       			elif ch == '}' and top =='{':
       				stack.pop()
       			else:
       				return False
       		else:
       		    return False
       	if len(stack) == 0:
       		return True
       	else:
       		return False
