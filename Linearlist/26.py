"""
    26. Remove Duplicates from Sorted Array

    @author: Shangru
    @date: 2015/09/13
"""
class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        index = 0
        for i in range(1, len(nums)):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]            
        return index+1