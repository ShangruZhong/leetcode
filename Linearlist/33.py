class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    	left = 0
    	right = len(nums)
    	while left!=right: 
    		mid = left+(right-left)/2
    		if target == nums[mid]:
    			return mid
    		if nums[left]<=nums[mid]: # nums[mid] in left sorted array
    			if nums[left]<=target and target<nums[mid]:
    				right = mid
    			else:
    				left = mid+1
    		else: #nums[mid] in right sorted array, and also the bounder
    			if nums[mid]<target and target<=nums[right-1]:
    				left = mid+1
    			else:
    				right = mid
    	return -1


a = [4,5,6,7,0,1,2]
obj = Solution()
print obj.search(a,0)
print obj.search(a,3)