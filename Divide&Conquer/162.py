"""
    162. Find Peak Element

    @date: 2017/06/06
"""
class Solution(object):
    # solution 1
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        for i in xrange(1, size):
            if nums[i] < nums[i - 1]:
                return  i - 1
        return size - 1

    # solution 2
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) / 2
            if nums[mid] < nums[mid + 1]:
                l = mid + 1
            else:
                r = mid
        return l