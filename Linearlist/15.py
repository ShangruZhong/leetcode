"""
	15. 3Sum

	@author: Shangru
	@date: 2015/09/19
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        for i in range(len(nums)-2):
        	if i==0 or nums[i]>nums[i-1]:
	 			left = i+1
	 			right = len(nums)-1
	 			while left<right:
	 				if nums[left]+nums[right]==-nums[i]:
	 					result.append([nums[i],nums[left],nums[right]])
	 					left += 1
	 					right -= 1
	 					while left<right and nums[left]==nums[left-1]:
	 						left += 1
	 					while left<right and nums[right]==nums[right+1]:
	 						right -= 1
	 				elif nums[left]+nums[right]<-nums[i]:
	 					while left<right:
	 						left += 1
	 						if nums[left]>nums[left-1]:
	 							break
	 				else:
	 					while left<right:
	 						right -=1
	 						if nums[right]<nums[right+1]:
	 							break

        return result

nums = [-1,0,1,2,-1,4]
obj = Solution()
print obj.threeSum(nums)
