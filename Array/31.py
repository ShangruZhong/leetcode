"""
    31. Next Permutation

    @date: 2017/04/21
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        if not size or size == 1:
            return
        ii = size - 1
        i = ii - 1
        while i >= 0:
            if nums[i] < nums[ii]:
                j = size - 1
                while nums[i] >= nums[j]:
                    j -= 1
                nums[i], nums[j] = nums[j], nums[i]
                nums[ii:] = list(reversed(nums[ii:]))
                return
            if i == 0:
                nums[:] = list(reversed(nums[:]))
                return
            i -= 1
            ii -= 1
        
        