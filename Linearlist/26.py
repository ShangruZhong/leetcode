class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums):
            for i in range(0,len(nums)):
                if i<len(nums)-1 and nums[i]==nums[i+1]:
                    for j in range(i+1,len(nums)):
                        nums[j-1]=nums[j]
                    del nums[-1]
            del nums[-1]
        return len(nums)
        