"""
	65. Valid Number

	Tricky solution,
	unless use DFA, Deterministic Finite Automaton
	for multiple pattern match problem 
	@date: 2017/02/04
"""
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try: 
            float(s)
        except ValueError: 
            return False
        else: 
            return True