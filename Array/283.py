"""
    283. Move Zeroes

    @date: 2017/06/13
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nz = 0
        for i in xrange(len(nums)):
            if nums[i] != 0:
                nums[nz] = nums[i]
                nz += 1
        while nz < len(nums):
            nums[nz] = 0
            nz += 1