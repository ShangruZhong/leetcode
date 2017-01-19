"""
    40. Combination Sum II

    Refer to 39, set prev to avoid use candidates more than once
    @date: 2016/11/06
"""
import copy
class Solution(object):
    def combinationSum2(self, candidates, target):
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

        prev = -1
        for i in range(start, len(nums)):
            if prev == nums[i]:
                continue 
            if diff < nums[i]: # cut
                return 
            prev = nums[i]
            tmp.append(nums[i])
            self.backtracking(nums, diff - nums[i], i + 1, tmp, result)
            tmp.pop()