"""
	81. Search in Rotated Sorted Array II

	@author: Shangru
	@date: 2015/09/20
"""
class Solution(object):
    def search(self, nums, target):
		left = 0
		right = len(nums)
		while left!=right: 
			mid = left+(right-left)/2
			if target == nums[mid]:
				return True
			if nums[left]<nums[mid]: # nums[mid] in left sorted array
				if nums[left]<=target and target<nums[mid]:
					right = mid
				else:
					left = mid+1
			elif nums[left]>nums[mid]: #nums[mid] in right sorted array, and also the bounder
				if nums[mid]<target and target<=nums[right-1]:
					left = mid+1
				else:
					right = mid
			else: #nums[left]=nums[mid]
				left += 1
		return False
