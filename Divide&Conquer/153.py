"""
    153. Find Minimum in Rotated Sorted Array
    
    No consider duplicate number
    @date: 2017/04/27
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        if size == 1:
            return nums[0]
        l, r = 0, size - 1
        mid = l
        while nums[l] >= nums[r]:
            if r - l == 1:
                return nums[r]
            mid = (l + r)/2
            if nums[mid] >= nums[l]:
                l = mid
            elif nums[mid] <= nums[r]:
                r = mid
        return nums[mid]