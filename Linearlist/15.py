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
        result = []
        if len(nums) < 3:
            return result
            
        nums.sort()
        
        for i in range(len(nums)-2):
   			left = i + 1
   			if i > 0 and nums[i] == nums[i - 1]:
   			    continue
	 		right = len(nums) - 1
	 		while left < right:
	 			if nums[left] + nums[right] < - nums[i]:
	 			    left += 1
	 			    while nums[left] == nums[left - 1] and left < right:
	 			        left += 1
	 			elif nums[left] + nums[right] > - nums[i]:
	 			    right -= 1
	 			    while nums[right] == nums[right + 1] and left < right:
	 			        right -= 1
	 			else:
	 			    result.append([nums[i], nums[left], nums[right]])
	 			    left += 1
	 			    right -= 1
	 			    while nums[left] == nums[left - 1] and nums[right] == nums[right + 1] and left < right:
	 			        left += 1
        return result
