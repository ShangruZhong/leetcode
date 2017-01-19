"""
	17. Letter Combinations of a Phone Number

	@date: 2016/08/23
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        mapping = {"0":" ", "1":"*", "2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        path = ""
        res = []
        def backtracking(digits, path, res):
            if digits == "": # leaf node, backtrack
                res.append(path)
                return
            for i in mapping[digits[0]]:
                backtracking(digits[1:], path + i, res)
        backtracking(digits, path, res)
        return res
