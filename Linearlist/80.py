class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==0:
            return 0
        index = 0
        count = 1
        for i in range(1,len(nums)):
            if nums[index] != nums[i]:
                count = 1
                index = index+1
                nums[index] = nums[i]
            elif count<2:
            	index = index+1
            	nums[index] = nums[i]
            	count = count+1
            else:
            	count = count+1
        return index+1
    
a=[1,1,1,1,2,2,2,2,3,3,3,3]
obj = Solution()
print obj.removeDuplicates(a)
