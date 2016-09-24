"""
	34. Search for a Range
	
	BinarySearch for upper bound and lower bound
	@date: 2013/09/23
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.lower(nums, target, 0, len(nums) - 1), self.upper(nums, target, 0, len(nums) - 1)]

    def lower(self, nums, target, start, end):
        if start > end:
        	return -1
        mid = (start + end) / 2
      	if nums[mid] == target:
      		if (mid > 0 and nums[mid - 1] != target) or mid == 0:
      			return mid
      		else:
      			end = mid - 1
        elif nums[mid] > target:
        	end = mid - 1
       	else:
       		start = mid + 1
        return self.lower(nums, target, start, end)

    def upper(self, nums, target, start, end):
        if start > end:
        	return -1
        mid = (start + end) / 2
        if nums[mid] == target:
        	if (mid < len(nums) - 1 and nums[mid + 1]!= target) or mid == len(nums) - 1:
        		return mid
        	else:
        		start = mid + 1
        elif nums[mid] < target:
        	start = mid + 1
        else:
        	end = mid - 1
        return self.upper(nums, target, start, end)