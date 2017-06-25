"""
    215. Kth Largest Element in an Array

    classical Top-K questions
    @date: 2017/06/10
"""
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        size = len(nums)
        l, r = 0, size - 1
        index = self.partition(nums, l, r)
        while index != size - k:
            if index > size - k:
                r = index - 1
            else:
                l = index + 1
            index = self.partition(nums, l, r)
        return nums[size - k]
    
    def partition(self, nums, left, right):
        x = nums[right]
        pivot = left - 1
        for i in xrange(left, right + 1):
            if nums[i] < x:
                pivot += 1
                nums[pivot], nums[i] = nums[i], nums[pivot]
        nums[pivot + 1], nums[right] = nums[right], nums[pivot + 1]
        return pivot + 1