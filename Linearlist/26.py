# This solution exceed the time limit, cannot be accepted!
class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums):
            for i in range(0,len(nums)):
                if i>=len(nums)-1:
                    break
                while nums[i]==nums[i+1]:
                    for j in range(i,len(nums)-1):
                        nums[j]=nums[j+1]
                    del nums[-1]
                    if i>=len(nums)-1:
                        break  
        return len(nums)
    
a=[1,1,1,1,2,2,2,2,3,3,3,3]
obj = Solution()
print obj.removeDuplicates(a)
