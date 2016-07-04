"""
	4. Median of Two Sorted Arrays
	
	@author: Shangru
	@date: 2016/07/04
"""
class Solution(object):
    def findKth(self, nums1, nums2, k):
	    if len(nums1) == 0:
	        return nums2[k - 1]
	    if len(nums2) == 0:
	        return nums1[k - 1]
	    if k == 1:
	        return min(nums1[0], nums2[0])
	    
	    a = nums1[k / 2 - 1] if len(nums1) >= k / 2 else None
	    b = nums2[k / 2 - 1] if len(nums2) >= k / 2 else None
	    
	    if b is None or (a is not None and a < b):
	        return self.findKth(nums1[k / 2:], nums2, k - k / 2)
	    return self.findKth(nums1, nums2[k / 2:], k - k / 2)
	    
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.findKth(nums1, nums2, n / 2 + 1)
        else:
            smaller = self.findKth(nums1, nums2, n / 2)
            bigger = self.findKth(nums1, nums2, n / 2 + 1)
            return (smaller + bigger) / 2.0
            
    # def median(self, nums):
    #     length = len(nums)
    #     if length % 2 == 1: # odd
    #         return nums[length/2]
    #     else: # even
    #         return 1/2.0*(nums[length/2 - 1] + nums[length/2])

s = Solution()
print s.findMedianSortedArrays([1,2,3],[3,4])
