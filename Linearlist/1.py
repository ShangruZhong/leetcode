"""
    1. Two Sum

    @author: Shangru
    @date: 2015/09/18
"""
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range(len(nums)):
        	if target-nums[i] in hashmap:
        		return (hashmap[target-nums[i]]+1,i+1)
        	hashmap[nums[i]] = i
