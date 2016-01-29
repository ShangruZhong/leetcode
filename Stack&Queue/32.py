"""
	32. Longest Valid Parentheses
	
	Using stack to judge Parentheses Matching Problem
	@author: Shangru
	@date: 2016/01/28
"""
class Solution(object):
	def longestValidParentheses(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		if s == "":
			return 0
		last = -1  # position of last un-matching ')'
		max_length = 0
		stack = []
		for i in xrange(len(s)):
			if s[i] == '(':
				stack.append(i)
			elif len(stack) == 0:
				last = i
			else:
				stack.pop()
				# after pop(), update max_length
				if len(stack) == 0:
					max_length = max(max_length, i-last) # distance between last un-matching ')' and current ')'
				else:
					max_length = max(max_length, i-stack[-1]) # distance between last un-matching '(' and current ')'
		return max_length


