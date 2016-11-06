"""
    39. Combination Sum

    target -= taget- candidates
    for each target, traverse all candidates
    @date: 2016/11/06
"""
import copy
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = list()
        tmp = list()
        candidates.sort() # key
        self.backtracking(candidates, target, 0, tmp, result)
        return result
    
    def backtracking(self, nums, diff, start, tmp, result):
        if diff == 0:
            a = copy.deepcopy(tmp)
            result.append(a)
            return
        for i in range(start, len(nums)):
            if diff < nums[i]: # cut
                return 
            tmp.append(nums[i])
            self.backtracking(nums, diff - nums[i], i, tmp, result)
            tmp.pop()
            